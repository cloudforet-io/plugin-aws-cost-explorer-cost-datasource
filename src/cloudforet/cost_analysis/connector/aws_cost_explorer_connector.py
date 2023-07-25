import logging
import boto3
from spaceone.core import utils
from spaceone.core.connector import BaseConnector
from spaceone.core.error import *

__all__ = ['AWSCostExplorerConnector']

_LOGGER = logging.getLogger(__name__)
_DEFAULT_REGION = 'us-east-1'


class AWSCostExplorerConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = None
        self.org_client = None
        self.ce_client = None
        self.sts_client = None

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

    def get_account_id(self):
        if self.sts_client is None:
            self.sts_client = self.session.client('sts')

        response = self.sts_client.get_caller_identity()
        return response.get('Account')

    def list_active_accounts(self):
        if self.org_client is None:
            self.org_client = self.session.client('organizations')

        accounts = []
        paginator = self.org_client.get_paginator('list_accounts')
        response_iterator = paginator.paginate()

        for response in response_iterator:
            for account in response.get('Accounts', []):
                if account.get('Status') == 'ACTIVE':
                    accounts.append(account)

        return accounts

    def get_cost_and_usage(self, **query):
        if self.ce_client is None:
            self.ce_client = self.session.client('ce')

        response = self.ce_client.get_cost_and_usage(**query)
        results_by_time = response.get('ResultsByTime', [])

        costs_data = self._convert_costs_data(results_by_time)
        yield costs_data

        if next_page_token := response.get('NextPageToken'):
            query.update({'NextPageToken': next_page_token})
            yield from self.get_cost_and_usage(**query)

    @staticmethod
    def _convert_costs_data(results_by_time):
        costs_data = []
        for result in results_by_time:
            time_period = result.get('TimePeriod', {})
            _groups = result.get('Groups', [])
            for _group in _groups:
                _group.update({'TimePeriod': time_period})
                costs_data.append(_group)

        return costs_data

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
