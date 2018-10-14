import os
import urllib.request
import shutil
import zipfile
import subprocess
from argparse import ArgumentParser
from sys import platform

pdev_dir = os.path.join(os.path.expanduser('~'), ('pdev'))

# pDev Tools
vscode_uri = 'https://go.microsoft.com/fwlink/?Linkid=850641'
vscode_extension_list_uri = '<insert github link here>'
rust_uri = 'https://win.rustup.rs'

def download_file(uri, out_path):
    print('Downloading...')
    with urllib.request.urlopen(uri) as response, open(out_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def download_extract_zip(uri, out_path):
    tmp_zip = os.path.join(pdev_dir, 'tmp.zip')
    download_file(uri, tmp_zip)

    # Make sure to create directory first if it doesn't already exists
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    print('Extracting to directory...', end='')
    with zipfile.ZipFile(tmp_zip, 'r') as zip_ref:
        zip_ref.extractall(out_path)
    
    if os.path.exists(tmp_zip):
        os.remove(tmp_zip)
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

def install_rust():
    print('Installing rust...')
    if platform == 'linux' or platform == 'linux2':
        print('Rust installation not supported for linux yet :(')
    elif platform == 'darwin':
        print('Rust installation not supported for macOS yet :(')
    elif platform == 'win32':
        rust_path = os.path.join(pdev_dir, 'rustup-init.exe')
        download_file(rust_uri, rust_path)
        if subprocess.call(rust_path) != 0:
            print('Rust installation failed?')
        else:
            print('Done')

def install_tools(tools=None):
    if 'all' in tools:
        print('Installing full pDev environment...')
        install_vscode()
        print('Done')
    else:
        if 'vscode' in tools:
            install_vscode()
        if 'rust' in tools:
            install_rust()
        if 'node' in tools:
            print('node install not supported')
            # install_node()
        if 'yarn' in tools:
            print('yarn install not supported')
            # install_yarn()

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
            _file.write('function pdev_func {Invoke-Expression "'+ pdev_dir + '\python\python.exe pdev.py $args"}\n')
            _file.write('Set-Alias -Name pdev -Value pdev_func\n')
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
