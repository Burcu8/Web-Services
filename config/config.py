from default import config as default_config
from development import config as dev_config
from production import config as prod_config
from env import config as envs
import os

environment = os.environ['PYTHON_ENV'] or 'development'
environment_config = None

#dict 

if environment == 'development':
    environment_config = dev_config
if environment == ' production':
    environment_config = prod_config

def chain_configs(*config_items):
    for item in config_items:
        for element in item:
            value = element[1]
            if value is not None:
                yield element

config = dict(chain_configs(*default_config.items(), environment_config.items, envs.items()))