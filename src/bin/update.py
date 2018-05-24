#!/bin/env python
#
___author__ = 'Adam Grigolato'
__version__ = '0'
#IMPORTS
import argparse
import sys
#



class TKM_update_Menu(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Toolkit Manager Updates',
            usage='''tkitman update <command> [<args>]

The most commonly used profile commands are:
   all       Update Everything (Toolkit tree, all toolkits, and tkitman itself)
   tree      Update the toolkit tree
   toolkit   Update a toolkit
   tkitman   Update tkitman itself
''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def all(self):
        parser = argparse.ArgumentParser(description='Update Everything')
        parser.add_argument('-f'.'--force', action='store_true',help='Force overwriting without user input')
        args = parser.parse_args(sys.argv[2:])

    def tree(self):
        parser = argparse.ArgumentParser(description='Update the toolkit tree')
        parser.add_argument('-url',action='store',help='(Optional), give me a url to fetch instead of my configured list')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def toolkit(self):
        parser = argparse.ArgumentParser(description='Update a toolkit')
        parser.add_argument('toolkit', action='store',help='Name of toolkit to update, all will update all toolkits')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def tkitman(self):
        parser = argparse.ArgumentParser(description='Update tkitman')
        args = parser.parse_args(sys.argv[2:])
        print('weee')


if __name__ == '__main__':
    Roll_Pro_Menu()
