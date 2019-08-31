import os

def read_boolean(variable_name, default:str=None):
    value = os.getenv(variable_name, default).lower()

    if value == 'true':
        return True
    elif value == 'false':
        return False
    else:
        raise ValueError('The boolean string value is not valid for configuration.')

def read_int(variable_name, default:str=None):
    value = os.getenv(variable_name, default)
    return int(value)

DEBUG = read_boolean('DEBUG', default='false')
ENABLE_DEBUGGER_ATTACH = read_boolean('ENABLE_DEBUGGER_ATTACH', default='false')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
PROPAGATE_EXCEPTIONS = read_boolean('PROPAGATE_EXCEPTIONS', default='true')
