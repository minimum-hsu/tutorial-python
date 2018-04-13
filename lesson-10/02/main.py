#!/usr/bin/env python3

import logging
from logging import config
import yaml


#######################################
# Config
#######################################
with open('logging.conf') as f:
    conf = yaml.load(f)
    config.dictConfig(conf)
log = logging.getLogger('demo')


if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
