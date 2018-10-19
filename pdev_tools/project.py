import os
import urllib
import subprocess
import pdev_tools.util as util
import pdev_tools.rust as rust
from sys import platform

class PDevTool_Project():

    def __init__(self):
        self.name = 'Project'
        self.cli_name = 'project'
    
    def install(self, dir):
        # Nothing to install
        return

    def init_argparser(self, parser):
        proj_parser = parser.add_parser('project', help='Project utitlies')
        sub = proj_parser.add_subparsers(title='Project Utitlies', dest='projectcmd')

        new_parser = sub.add_parser('new', help='Create new project')
        new_parser.add_argument('--rust', action='store_true', help='New rust application')
        new_parser.add_argument('--cpp', action='store_true', help='New c++ application')
        new_parser.add_argument('--csharp', action='store_true', help='New c# application')
        new_parser.add_argument('--reactjs', action='store_true', help='New react js application')
        new_parser.add_argument('--react-native', action='store_true', help='New react native application')

    def parse_args(self, args, dir):
        if args.toolcmd == 'project':
            print(args)
            if args.projectcmd == 'new':
                print('not supported')
        return

def __init_tool():
    return PDevTool_Project()