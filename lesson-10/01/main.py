#!/usr/bin/env python3

import logging


logging.basicConfig(
    format = '%(asctime)s [%(levelname)s] %(message)s',
    datefmt = '%Y/%m/%dT%H:%M:%S',
    level = logging.INFO
)
 
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
