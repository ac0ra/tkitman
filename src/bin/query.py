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
import msgpack
import yaml
#



class TK_Query_Menu(object):

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
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def list(self):
        parser = argparse.ArgumentParser(description='List a property')
        parser.add_argument('-f','--file',action='store',help='Filename to query if desired (WILL BE REMOVED)')
        parser.add_argument('-y','--yaml',action='store',help='Print yaml?')
        parser.add_argument('list',action='store',help='list to access')
        args = parser.parse_args(sys.argv[2:])
        if not (args.file):
            if args.list == 'toolkits':
                import tkitman
                tk = tkitman.config()
                print('::List of toolkits::\n'+yaml.dump(msgpack.unpackb(tk.core['toolkit_listfile'])))
        else:
            with open(args.file,'rb') as msgpackf:
                list = msgpack.unpackb(msgpackf.read(), raw = False)
                print('::FILE LIST::'+yaml.dump(list))
                

    def get(self):
        parser = argparse.ArgumentParser(description='Get a configuration setting')
        parser.add_argument('profile')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def search(self):
        parser = argparse.ArgumentParser(description='Modify profile config.')
        parser.add_argument('--insert_argument_here')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def info(self):
        parser = argparse.ArgumentParser(description='Export profile to a file, (config only, or config and scripts).')
        parser.add_argument('--insert_argument_here')
        args = parser.parse_args(sys.argv[2:])
        print('weee')


if __name__ == '__main__':
    TK_Query_Menu()
