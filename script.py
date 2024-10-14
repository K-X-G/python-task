import logging
import logging.config
import yaml

# Task 1: Read from configuration file
# logging.config.fileConfig('logging.conf')
with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# Create logger
logger = logging.getLogger('staging')

# Main
# Task 2: Gather data from API

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
