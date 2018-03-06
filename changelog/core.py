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

def isApplied(package, version, package_date):
    if len(search(package, version, package_date)) > 0:
        return True
    else:
        return False


def search(package, version, package_date):

    try:
        Package = Query()
        packages = db.table('packages')
        return packages.search((Package.name == package) & (Package.version == version) & (Package.package_date == package_date))
    except Exception as e:
        _logger.error(e)
        raise


def insert(package):

    try:
        ts = datetime.datetime.now().isoformat()
        packages = db.table('packages')
        package['timestamp'] = ts
        return packages.insert(package)
    except Exception as e:
        _logger.error(e)
        raise


def history():

    try:
        Package = Query()
        packages = db.table('packages')
        return packages.all()
        # return packages.search(Package.name.search('.*'))
    except IndexError:
        _logger.error(e)
        pass
