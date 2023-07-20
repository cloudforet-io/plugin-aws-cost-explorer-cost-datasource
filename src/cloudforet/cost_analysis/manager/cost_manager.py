import logging
from datetime import datetime, timedelta
from spaceone.core.error import *
from spaceone.core.manager import BaseManager
from cloudforet.cost_analysis.connector.aws_cost_explorer_connector import AWSCostExplorerConnector
from cloudforet.cost_analysis.conf.cost_conf import *

_LOGGER = logging.getLogger(__name__)

class CostManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aws_ce_connector: AWSCostExplorerConnector = self.locator.get_connector('AWSCostExplorerConnector')

    def get_data(self, options, secret_data, schema, task_options):
        self.aws_ce_connector.create_session(options, secret_data, schema)
        self._check_task_options(task_options)

        account_id = task_options['account_id']
        start = task_options['start']

        _end = datetime.utcnow() + timedelta(days=5)
        end = _end.strftime('%Y-%m-%d')

        cost_query = self._set_query(account_id, start, end)
        print(f'[get_data] cost_query: {cost_query}')

        for costs_data in self._get_cost_and_usage(cost_query):
            yield self._make_cost_data(costs_data, account_id)

    def _get_cost_and_usage(self, query):
        while True:
            print(f'[_get_cost_and_usage] query: {query}')
            results = self.aws_ce_connector.get_cost_and_usage(**query)
            print(f'[_get_cost_and_usage] results via AWS CE: {len(results)}')
            costs_data, is_continue, next_start = self._get_costs_data(results)
            yield costs_data

            if is_continue and next_start:
                query['TimePeriod']['Start'] = next_start
            else:
                break

    @staticmethod
    def _get_costs_data(results):
        is_continue = False
        next_start = None
        costs_data = []

        for result in results:
            time_period = result.get('TimePeriod', {})

            if len(costs_data) > AWS_COST_DATA_MAX_PAGE:
                print(f'[_get_costs_data] is continue and next_start: {time_period.get("Start")}')
                is_continue = True
                next_start = time_period.get('Start')
                break
            else:
                # print(f'[_get_costs_data] costs_data: {len(costs_data)}, time: {time_period}')
                _groups = result.get('Groups', [])
                for _group in _groups:
                    _group.update({'TimePeriod': time_period})

                costs_data.extend(_groups)

        return costs_data, is_continue, next_start

    def _make_cost_data(self, costs_data, account_id):
        costs_info = []

        """ Source Data Model
        class CostSummaryItem(BaseModel):
            billed_at: datetime
            region: str
            service_code: str
            usage_type: str
            usage_unit: str
            instance_type: str
            tag_application: str
            tag_environment: str
            tag_name: str
            tag_role: str
            tag_service: str
            usage_quantity: float
            usage_cost: float
        """
        for _cost in costs_data:
            try:
                time_period = _cost.get('TimePeriod', {})
                product, raw_usage_type = self._get_info_from_group_key(_cost)
                metrics_info = _cost.get('Metrics', {})
                cost, currency = self._get_cost_info_from_metric(metrics_info)
                usage_quantity, usage_unit = self._get_usage_info_from_metric(metrics_info)

                data = {
                    'cost': cost,
                    'currency': currency,
                    'usage_quantity': usage_quantity,
                    'usage_type': raw_usage_type,
                    'usage_unit': usage_unit,
                    'provider': 'aws',
                    'account': account_id,
                    'product': product,
                    'resource': '',
                    'billed_at': self._set_billed_at(time_period.get('Start')),
                    'additional_info': self._get_additional_info(product, raw_usage_type),
                    'tags': {}
                }

                costs_info.append(data)
            except Exception as e:
                _LOGGER.error(f'[_make_cost_data] make data error: {e}', exc_info=True)
                raise e

        print(f'[_make_cost_data][{account_id}] costs_info length: {len(costs_info)}')
        return costs_info

    def get_region_list(self, account_id, start, end):
        region_query = self._set_region_query(account_id, start, end)
        azs = []

        print(f'[get_region_list] region_query: {region_query}')

        for results in self.aws_ce_connector.get_cost_and_usage(**region_query):
            for result in results:
                for group in result.get('Groups', []):
                    az = group.get('Keys', [])[0]
                    if az == 'NoAZ':
                        azs.append('global')
                    else:
                        azs.append(az)

        regions = []
        for az in list(set(azs)):
            if az[-1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                regions.append(az)
            else:
                regions.append(az[:-1])

        print(f'[get_region_list] regions: {list(set(regions))}')
        return list(set(regions))

    @staticmethod
    def _get_info_from_group_key(group):
        keys = group.get('Keys', [])
        service_name = keys[0]
        raw_usage_type = keys[1]

        if service_name == 'EC2 - Other':
            service_name = 'AmazonEC2'
        elif service_name == 'Amazon Elastic Compute Cloud - Compute':
            service_name = 'AmazonEC2'
        elif service_name == 'Amazon Elastic Container Service for Kubernetes':
            service_name = 'AmazonEKS'

        return service_name, raw_usage_type

    def _set_region_query(self, account_id: str, start: str, end: str):
        _query = self._set_default_query(account_id, start, end)
        _query.update({'GroupBy': [{'Type': 'DIMENSION', 'Key': 'AZ'}]})

        return _query

    def _set_query(self, account_id: str, start: str, end: str):
        _query = self._set_default_query(account_id, start, end)
        _query.update({'Filter': {'Dimensions': {'Key': 'LINKED_ACCOUNT', 'Values': [account_id]}}})

        for dimension in GROUP_BY_DIMENSIONS:
            _query['GroupBy'].append({
                'Type': 'DIMENSION',
                'Key': dimension
            })

        return _query

    def _set_query_with_region(self, account_id: str, region_code: str, start: str, end: str):
        _query = self._set_default_query(account_id, start, end)

        _query.update({'Filter': {'And': [
            {
                'Dimensions': {
                    'Key': 'LINKED_ACCOUNT',
                    'Values': [account_id]
                }
            },
            {
                'Dimensions': {
                    'Key': 'REGION',
                    'Values': [region_code]
                }
            }
        ]}})

        for dimension in GROUP_BY_DIMENSIONS:
            _query['GroupBy'].append({
                'Type': 'DIMENSION',
                'Key': dimension
            })

        return _query

    @staticmethod
    def _get_cost_info_from_metric(metrics):
        _cost_info = metrics.get(COST_METRIC, {})
        return _cost_info.get('Amount', 0), _cost_info.get('Unit', 'USD')

    @staticmethod
    def _get_usage_info_from_metric(metrics):
        _usage_info = metrics.get(USAGE_METRIC, {})
        return _usage_info.get('Amount', 0), _usage_info.get('Unit')

    @staticmethod
    def _set_default_query(account_id: str, start: str, end: str):
        return {
            'TimePeriod': {
                'Start': start,
                'End': end
            },
            'Filter': {
                'Dimensions': {
                    'Key': 'LINKED_ACCOUNT',
                    'Values': [account_id]
                }
            },
            'Granularity': GRANULARITY,
            'Metrics': METRICS,
            'GroupBy': [],
        }

    @staticmethod
    def _set_billed_at(start: str):
        try:
            return datetime.strptime(start, '%Y-%m-%d')
        except Exception as e:
            _LOGGER.error(f'[_set_billed_at] set billed_at error: {e}', exc_info=True)
            return None

    @staticmethod
    def _get_additional_info(product, usage_type):
        additional_info = {}
        instance_type = None

        if 'BoxUsage:' in usage_type:
            instance_type = usage_type.split('BoxUsage:')[-1]
        elif product == 'Amazon CloudFront':
            if usage_type.find('-HTTPS') > 0:
                instance_type = 'requests.https'
            elif usage_type.find('-Out-Bytes') > 0:
                instance_type = 'data-transfer.out'
            else:
                instance_type = 'requests.http'
        else:
            if usage_type.find('-In-Bytes') > 0:
                instance_type = 'data-transfer.in'
            elif usage_type.find('-Out-Bytes') > 0:
                instance_type = 'data-transfer.out'
            elif usage_type.find('-Bytes') > 0 \
                    and usage_type.find('-DataProcessing-') == -1 and usage_type.find('-DataScanned-') == -1:
                instance_type = 'data-transfer.etc'

        if instance_type:
            additional_info.update({'Instance Type': instance_type})

        return additional_info

    @staticmethod
    def _check_task_options(task_options):
        if 'account_id' not in task_options:
            raise ERROR_REQUIRED_PARAMETER(key='task_options.account_id')

        if 'start' not in task_options:
            raise ERROR_REQUIRED_PARAMETER(key='task_options.start')
