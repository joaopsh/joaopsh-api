
from libs.text_resource import TextResource

from constants.api_status import ERROR
from constants.api_error import INTERNAL_SERVER_ERROR

def error_handler(exception):
    return {
        'status': ERROR,
        'data': {
            'id': INTERNAL_SERVER_ERROR.id,
            'code': INTERNAL_SERVER_ERROR.code,
            'description': TextResource.get_text(INTERNAL_SERVER_ERROR.id)
        }
    }, 500
