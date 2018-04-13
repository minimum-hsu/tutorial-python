#!/usr/bin/env python3

import logging


#######################################
# Config
#######################################
logging.basicConfig(
    format = '%(asctime)s [%(levelname)s] %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S%z',
    level = logging.INFO
)


if __name__ == '__main__':
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')

    try:
        1 / 0
    except Exception as err:
        logging.exception(err)
