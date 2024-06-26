import logging
import pytz
from datetime import datetime, timedelta

from spaceone.core.manager import BaseManager
from cloudforet.cost_analysis.error import *
from cloudforet.cost_analysis.conf.cost_conf import SECRET_TYPE_DEFAULT
from cloudforet.cost_analysis.connector.aws_cost_explorer_connector import AWSCostExplorerConnector
from cloudforet.cost_analysis.model.job_model import Tasks

_LOGGER = logging.getLogger(__name__)


class JobManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aws_ce_connector: AWSCostExplorerConnector = self.locator.get_connector(AWSCostExplorerConnector)

    def get_tasks(self, options, secret_data, schema, start, last_synchronized_at, domain_id):
        tasks = []
        changed = []

        start_time = self._get_start_time(start, last_synchronized_at)
        start_date = start_time.strftime('%Y-%m-%d')
        changed_time = start_time.strftime('%Y-%m')

        # For compatibility
        # self._check_options(options)
        secret_type = options.get('secret_type', SECRET_TYPE_DEFAULT)

        if secret_type == 'MANUAL':
            self.aws_ce_connector.create_session(options, secret_data, schema)

            for account_info in self.aws_ce_connector.list_active_accounts():
                tasks.append({'task_options': {'account_id': account_info['Id'], 'start': start_date}})
                changed.append({'start': changed_time})

        elif secret_type == 'USE_SERVICE_ACCOUNT_SECRET':
            self.aws_ce_connector.create_session(options, secret_data, schema)
            aws_account_id = self.aws_ce_connector.get_account_id()
            tasks.append({'task_options': {'account_id': aws_account_id, 'start': start_date}})
            changed.append({
                'start': changed_time,
                'filter': {
                    'additional_info.account_id': aws_account_id
                }
            })
        else:
            raise ERROR_INVALID_SECRET_TYPE(secret_type=options.get('secret_type'))

        tasks = Tasks({'tasks': tasks, 'changed': changed})
        tasks.validate()
        return tasks.to_primitive()

    @staticmethod
    def _get_start_time(start, last_synchronized_at=None):

        if start:
            max_start_time: datetime = datetime.utcnow() - timedelta(days=365)
            max_start_time = max_start_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)

            if start < max_start_time:
                raise ERROR_INVALID_PARAMETER(key='start', reason='start date is too old. (Max: 12 months)')

            start_time: datetime = start
        elif last_synchronized_at:
            start_time: datetime = last_synchronized_at - timedelta(days=7)
            start_time = start_time.replace(day=1)
        else:
            start_time: datetime = datetime.utcnow() - timedelta(days=365)
            start_time = start_time.replace(day=1)

        start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

        return start_time

    # @staticmethod
    # def _check_options(options):
    #     if secret_type := options.get('secret_type'):
    #         if secret_type not in ['MANUAL', 'USE_SERVICE_ACCOUNT_SECRET']:
    #             raise ERROR_INVALID_SECRET_TYPE(secret_type=secret_type)
    #
    #     else:
    #         raise ERROR_REQUIRED_PARAMETER(key='options.secret_type')
