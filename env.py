import os


def get_env(var, default=None):
    return os.environ[var]

config = {
    'app_name': get_env('APP_NAME'),
    'host': get_env('HOST'),
    'port': get_env('PORT')
}