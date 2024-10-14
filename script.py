import logging
import logging.config
import yaml
import requests
from requests.exceptions import SSLError
import os

# Task 1: Read from configuration file
# logging.config.fileConfig('logging.conf')
with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# Create logger
logger = logging.getLogger('staging')

# Main
# Task 2: Gather data from API
ip_address = os.environ.get("FIND_IP_LOCATION", "151.237.67.254")
url = f"https://ipapi.co/{ip_address}/json/"

try:
    loc = requests.get(url)
    print(loc.json())
except SSLError as err:
    logger.error(f"An SSLError occurred: {err}")
    

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
