#!/bin/env python
# coding: utf-8
# Usage: tkitman query utility
# Help: 
# list    -- Lists tkits and other data.
# get     -- Get a configuation setting.
# search  -- Search configuration or metadata.
# info    -- print metadata for tkits.

#
___author__ = 'Adam Grigolato'
__version__ = '0'
#IMPORTS
import argparse
import sys
#



class ROLL_Pro_Menu(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='tkitman query utility',
            usage='''tkitman query <command> [<args>]

The most commonly used query commands are:
   list     -- Lists tkits and other data.
   get      -- Get a configuration setting.
   search   -- Search configuration or metadata.
   info     -- Print metadata for tkits.
''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def add(self):
        parser = argparse.ArgumentParser(description='List a property')
        parser.add_argument('list', action='store_true')
        args = parser.parse_args(sys.argv[2:])

    def remove(self):
        parser = argparse.ArgumentParser(description='Remove a profile.')
        parser.add_argument('profile')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def edit(self):
        parser = argparse.ArgumentParser(description='Modify profile config.')
        parser.add_argument('--insert_argument_here')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def export(self):
        parser = argparse.ArgumentParser(description='Export profile to a file, (config only, or config and scripts).')
        parser.add_argument('--insert_argument_here')
        args = parser.parse_args(sys.argv[2:])
        print('weee')


if __name__ == '__main__':
    Roll_Pro_Menu()
