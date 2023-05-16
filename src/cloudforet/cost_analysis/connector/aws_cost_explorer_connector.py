import logging
import boto3
from spaceone.core import utils
from spaceone.core.connector import BaseConnector
from spaceone.core.error import *
from cloudforet.cost_analysis.conf.cost_conf import *

__all__ = ['AWSCostExplorerConnector']

_LOGGER = logging.getLogger(__name__)
_DEFAULT_REGION = 'us-east-1'


class AWSCostExplorerConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = None
        self.org_client = None
        self.ce_client = None

    def create_session(self, options: dict, secret_data: dict, schema: str):
        self._check_secret_data(secret_data)

        aws_access_key_id = secret_data['aws_access_key_id']
        aws_secret_access_key = secret_data['aws_secret_access_key']
        role_arn = secret_data.get('role_arn')
        external_id = secret_data.get('external_id')

        if role_arn:
            self._create_session_aws_assume_role(aws_access_key_id, aws_secret_access_key, _DEFAULT_REGION,
                                                 role_arn, external_id)
        else:
            self._create_session_aws_access_key(aws_access_key_id, aws_secret_access_key, _DEFAULT_REGION)

        self.ce_client = self.session.client('ce')
        self.org_client = self.session.client('organizations')

    def list_active_accounts(self):
        accounts = []
        paginator = self.org_client.get_paginator('list_accounts')
        response_iterator = paginator.paginate()

        for response in response_iterator:
            for account in response.get('Accounts', []):
                if account.get('Status') == 'ACTIVE':
                    accounts.append(account)

        return accounts

    def get_cost_and_usage(self, **query):
        response = self.ce_client.get_cost_and_usage(**query)
        results_by_time = response.get('ResultsByTime', [])

        page_count = int(len(results_by_time) / PAGE_SIZE) + 1

        for page_num in range(page_count):
            offset = PAGE_SIZE * page_num
            yield results_by_time[offset:offset + PAGE_SIZE]

    @staticmethod
    def _check_secret_data(secret_data):
        if 'aws_access_key_id' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.aws_access_key_id')

        if 'aws_secret_access_key' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.aws_secret_access_key')

    def _create_session_aws_access_key(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.session = boto3.Session(aws_access_key_id=aws_access_key_id,
                                     aws_secret_access_key=aws_secret_access_key,
                                     region_name=region_name)

        sts = self.session.client('sts')
        sts.get_caller_identity()

    def _create_session_aws_assume_role(self, aws_access_key_id, aws_secret_access_key, region_name, role_arn, external_id):
        self._create_session_aws_access_key(aws_access_key_id, aws_secret_access_key, region_name)

        sts = self.session.client('sts')

        _assume_role_request = {
            'RoleArn': role_arn,
            'RoleSessionName': utils.generate_id('AssumeRoleSession'),
        }

        if external_id:
            _assume_role_request.update({'ExternalId': external_id})

        assume_role_object = sts.assume_role(**_assume_role_request)
        credentials = assume_role_object['Credentials']

        self.session = boto3.Session(aws_access_key_id=credentials['AccessKeyId'],
                                     aws_secret_access_key=credentials['SecretAccessKey'],
                                     region_name=region_name,
                                     aws_session_token=credentials['SessionToken'])
