import logging
import logging.config
import yaml
import requests
from requests.exceptions import SSLError
import os
import mysql.connector
from mysql.connector import errorcode

# Task 1: Read from configuration file
# logging.config.fileConfig('logging.conf')
with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# Create logger
logger = logging.getLogger('staging')

def connect_to_mysql():
    try:
        return mysql.connector.connect(user='root', password='my-secret-pw', database='ip', host='mysql')        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error('Database does not exist')
        elif err.errno == errorcode.CR_CONN_HOST_ERROR:
            logger.error('Check if database server is running.')
        else:
            logger.error('Unknown error: ', err)

# Main
# Task 2: Gather data from API
ip_address = os.environ.get("FIND_IP_LOCATION", "8.8.8.8")
url = f"https://ipapi.co/{ip_address}/json/"

try:
    loc = requests.get(url)
    print(loc.json())
except SSLError as err:
    logger.error(f"An SSLError occurred: {err}")

query_stmt = ("INSERT INTO ip_location "
              "(ip, country, org) "
              "VALUES (%(ip)s, %(country_name)s, %(org)s)")
    
# Task 3: Write the result to SQL database
conn = connect_to_mysql()
if conn and conn.is_connected():
    logger.info('Connection to db is successful!')
    with conn.cursor() as cursor:
        try:
            logger.info('Inserting data into database...')
            cursor.execute(query_stmt, loc.json())

            # Make sure data is committed to the database
            conn.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                logger.error('Table does not exist!')
            else:
                logger.error('Unknown error: ', err)
        finally:
            cursor.close()

    conn.close()
else:
    logger.info('Could not connect.')

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
