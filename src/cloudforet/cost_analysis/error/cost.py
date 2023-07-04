from spaceone.core.error import *


class ERROR_CONNECTOR_CALL_API(ERROR_UNKNOWN):
    _message = 'API Call Error: {reason}'

class ERROR_INVALID_SECRET_TYPE(ERROR_INVALID_ARGUMENT):
    _message = 'Invalid secret type: {secret_type}'
