import logging

from spaceone.core.manager import BaseManager
from cloudforet.cost_analysis.model.data_source_model import PluginMetadata
from cloudforet.cost_analysis.connector.aws_cost_explorer_connector import AWSCostExplorerConnector

_LOGGER = logging.getLogger(__name__)


class DataSourceManager(BaseManager):

    @staticmethod
    def init_response(options):
        plugin_metadata = PluginMetadata()
        plugin_metadata.validate()

        return {
            'metadata': plugin_metadata.to_primitive()
        }

    def verify_plugin(self, options, secret_data, schema):
        aws_ce_connector: AWSCostExplorerConnector = self.locator.get_connector(AWSCostExplorerConnector)
        aws_ce_connector.create_session(options, secret_data, schema)
