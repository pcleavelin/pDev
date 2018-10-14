import os
import urllib.request
import shutil
import zipfile
from argparse import ArgumentParser
from sys import platform

pdev_dir = os.path.join(os.path.expanduser('~'), ('pdev'))

# pDev Tools
vscode_uri = 'https://go.microsoft.com/fwlink/?Linkid=850641'
vscode_extension_list_uri = '<insert github link here>'
rust_uri = '<insert rust curl url here>'

def download_extract_zip(uri, out_path):
    print('Downloading...')
    with urllib.request.urlopen(uri) as response, open('tmp.zip', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    # Make sure to create directory first if it doesn't already exists
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    print('Extracting to directory...', end='')
    with zipfile.ZipFile('tmp.zip', 'r') as zip_ref:
        zip_ref.extractall(out_path)
    
    if os.path.exists('tmp.zip'):
        os.remove('tmp.zip')
    print('Done')

def install_vscode():
    print('Installing VSCode...')
    download_extract_zip(vscode_uri, 'vscode')

    print('Creating data folder...', end='')
    if not os.path.exists('vscode/data'):
        os.makedirs('vscode/data')
    print('Done')

    vscode_dir = os.path.join(pdev_dir, 'vscode')
    print('VSCode installed to ' + vscode_dir)

def install_tools(tools=None):
    if 'all' in tools:
        print('Installing full pDev environment...')
        install_vscode()
        print('Done')
    else:
        if 'vscode' in tools:
            install_vscode()
        if 'rust' in tools:
            print('rust install not supported')
            # install_rust()
        if 'node' in tools:
            print('node install not supported')
            # install_node()
        if 'yarn' in tools:
            print('yarn install not supported')
            # install_yarn()

def add_alias():
    if platform == 'linux' or platform == 'linux2':
        print('Adding alias for linux not supported yet :(');
    elif platform == 'darwin':
        print('Adding alias for macOS not supported yet :(');
    elif platform == 'win32':
        profile_path = os.path.join(os.path.expanduser('~'), 'Documents\\WindowsPowerShell\\profile.ps1')

        with open(profile_path, 'a') as _file:
            _file.write('function pdev_func {Invoke-Expression "'+ pdev_dir + '\python\python.exe pdev.py -h"}\n')
            _file.write('Set-Alias -Name pdev -Value pdev_func\n');
        print('Added PowerShell alias \'pdev\'. Restart shell to see changes')

def tool_list(string):
    values = string.split(',')
    return values

parser = ArgumentParser(description='The pDev environment')
parser.add_argument('--install', metavar='TOOLS', type=tool_list, help='List of tools to install. \'--install all\' for full installation')
parser.add_argument('-alias', action='store_true', help='Creates a \'pdev\' alias for your terminal.')

args = parser.parse_args()

if args.install is not None:
    install_tools(args.install)
if args.alias:
    add_alias()
