import os
import urllib.request
import shutil
import zipfile
import subprocess
import sys
from argparse import ArgumentParser
from sys import platform

pdev_dir = os.path.join(os.path.expanduser('~'), ('pdev'))

sys.path.append(pdev_dir)

import pdev_tools
from pdev_tools import *

# pDev Tools
vscode_uri = 'https://go.microsoft.com/fwlink/?Linkid=850641'
vscode_extension_list_uri = 'https://gist.githubusercontent.com/pcleavelin/8d08dd2436aedc67f43615c1a1600da6/raw/9aa91fb16b50d31955667c479ca3df917885bf55/VSCode_Extensions.txt'
vscode_user_settings_uri = 'https://gist.githubusercontent.com/pcleavelin/8d08dd2436aedc67f43615c1a1600da6/raw/9aa91fb16b50d31955667c479ca3df917885bf55/VSCode_Settings.json'
rust_uri = '<insert rust curl url here>'

def install_tools(tools=None):
    if 'all' in tools:
        print('Installing full pDev environment...')
        for tool in pdev_tools.all_tools:
            tool.install(pdev_dir)
        print('Done')
    else:
        for tool in pdev_tools.all_tools:
            if tool.name in tools:
                tool.install(pdev_dir)


def add_alias():
    if platform == 'linux' or platform == 'linux2':
        print('Adding alias for linux not supported yet :(')
    elif platform == 'darwin':
        print('Adding alias for macOS not supported yet :(')
    elif platform == 'win32':
        profile_path = os.path.join(os.path.expanduser('~'), 'Documents\\WindowsPowerShell')
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)

        with open(profile_path + "\\profile.ps1", 'a') as _file:
            _file.write('function pdev_func {Invoke-Expression "'+ pdev_dir + '\\python\\python.exe pdev.py $args"}\n')
            _file.write('Set-Alias -Name pdev -Value pdev_func\n')
        print('Added PowerShell alias \'pdev\'. Restart shell to see changes')

def tool_list(string):
    values = string.split('/')
    return values

parser = ArgumentParser(description='The pDev environment')
parser.add_argument('--install', metavar='TOOLS', type=tool_list, help='List of tools to install. \'--install all\' for full installation')

command_parser = parser.add_subparsers(title='Tool Commands', dest='toolcmd', help='Tool Commands')
for tool in pdev_tools.all_tools:
    tool.init_argparser(command_parser)

args = parser.parse_args()

if args.install is not None:
    install_tools(args.install)
else:
    for tool in pdev_tools.all_tools:
        tool.parse_args(args, pdev_dir)
