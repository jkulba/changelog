#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, zipfile, subprocess, argparse, json, pprint, logging, logging.config
from changelog import core

'''example of changelog usage

Usage:
  changelog --package <filepath>
  changelog -h | --help
  changelog --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -m --manifest Show version.
'''

__version__ = "0.1.0"
__author__ = "James Kulba"

# create logger
logger = logging.getLogger('changeLog')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create file handler and set level to debug
fh = logging.FileHandler('changelog.log')
fh.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add formatter to fh
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

pp = pprint.PrettyPrinter(indent=2)

class Changeme(object):

    '''The Changeme object'''

    def __init__(self):
        logger.info('Changelog tool initializing')

    def load_manifest(self, path):

        with open(path) as json_file:
            data = json.load(json_file)
            name = data['name']
            version = data['version']
            package_date = data['package_date']
            package = {
                "name" : name,
                "version" : version,
                "package_date" : package_date
            }

            # doc_id = core.insert(package)
            # logger.info("Created doc: " + str(doc_id))

            # s = core.search(name, version, package_date)
            # pp.pprint(s)

            h = core.history()
            pp.pprint(h)





def main():
    '''Main entry point for the changelog CLI.'''
    parser = argparse.ArgumentParser(
        prog='Example Changelog Usage',
        description='Execute example changelog',
        usage='%(prog)s [options]')
    parser.add_argument('--manifest', dest='manifest_path', action='store',  required=True, help='Required parameter of the complete path of manifest file.')
    parser.add_argument('--version',
        action='version',
        version='%(prog)s ' + __version__)
    args = parser.parse_args()

    changeme = Changeme()

    if args.manifest_path:
        changeme.load_manifest(args.manifest_path)



if __name__ == '__main__':
    main()
