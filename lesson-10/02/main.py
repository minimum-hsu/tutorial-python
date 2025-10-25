#!/usr/bin/env python3



#############################
# Logging
#############################
import logging
from logging import config
from pathlib import Path
import yaml

workdir = Path(__file__).parent
with open(workdir / 'logging.conf') as f:
    conf = yaml.safe_load(f)
    config.dictConfig(conf)
log = logging.getLogger('demo')

#############################
# Main
#############################
if __name__ == '__main__':
    log.debug('debug')  # This will not be shown due to log level
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
