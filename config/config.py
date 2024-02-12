from config.default import config as default_config
from config.development import config as dev_config
from config.production import config as prod_config
import os

def get_config(config_name = 'development'):
    environment = os.environ['PYTHON_ENV'] or config_name
    environment_config = None
 

    if environment == 'development':
        environment_config = dev_config
    elif environment == 'production':
        environment_config = prod_config

    elif environment == 'test':
        environment_config = test_config

    return environment_config


    

