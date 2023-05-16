CONNECTORS = {
    'SpaceONEConnector': {},
    'AWSS3Connector': {}
}

LOG = {
    'filters': {
        'masking': {
            'rules': {
                'DataSource.verify': [
                    'secret_data'
                ],
                'Job.get_tasks': [
                    'secret_data'
                ],
                'Cost.get_data': [
                    'secret_data'
                ]
            }
        }
    }
}
