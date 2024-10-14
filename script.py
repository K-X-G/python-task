import logging
import logging.config
import yaml
import requests

# Task 1: Read from configuration file
# logging.config.fileConfig('logging.conf')
with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# Create logger
logger = logging.getLogger('staging')

# Main
# Task 2: Gather data from API
ip_address = input("Please enter the ip address: ")
url = f"https://ipapi.co/{ip_address}/json/"
loc = requests.get(url)
print(loc)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
