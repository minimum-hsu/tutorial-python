#!/usr/bin/env python3

#############################
# Logging
#############################
import logging
logging.basicConfig(
    format = '%(asctime)s [%(levelname)s] %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S%z',
    level = logging.INFO
)

#############################
# Main
#############################
if __name__ == '__main__':
    logging.debug('debug')  # This will not be shown due to log level
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')

    try:
        1 / 0
    except Exception as err:
        logging.exception(err)
