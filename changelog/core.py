# -*- coding: utf-8 -*-
import logging, datetime
from tinydb import TinyDB, Query

db = TinyDB('db.json')

__author__ = "James Kulba"

# Module version
__version__ = '${version}'

# Prepare the module logger
# _logger = logging.getLogger(__name__)
_logger = logging.getLogger('changeLog')

def search(package, version):
    _logger.info('Hit seach method.')

def insert(package):
    ts = datetime.datetime.now().isoformat()
    _logger.debug('Current time: ' + ts)

    db.insert(package)

def history():
    pass
