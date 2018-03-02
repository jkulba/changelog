#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, zipfile, subprocess, shlex, argparse, json, pprint, logging, logging.config
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

def main():
    '''Main entry point for the changelog CLI.'''
    parser = argparse.ArgumentParser(
        prog='Example Changelog Usage',
        description='Execute Device Updater',
        usage='%(prog)s [options]')
    parser.add_argument('--package', dest='package_path', action='store',  required=True, help='Required parameter to complete path and package file.')
    parser.add_argument('--version',
        action='version',
        version='%(prog)s ' + __version__)
    args = parser.parse_args()

if __name__ == '__main__':
    main()