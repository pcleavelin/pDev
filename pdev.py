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
vscode_extension_list_uri = 'https://gist.githubusercontent.com/pcleavelin/8d08dd2436aedc67f43615c1a1600da6/raw/9aa91fb16b50d31955667c479ca3df917885bf55/VSCode_Extensions.txt'
vscode_user_settings_uri = 'https://gist.githubusercontent.com/pcleavelin/8d08dd2436aedc67f43615c1a1600da6/raw/9aa91fb16b50d31955667c479ca3df917885bf55/VSCode_Settings.json'
rust_uri = '<insert rust curl url here>'

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
    vscode_dir = os.path.join(pdev_dir, 'vscode')

    download_extract_zip(vscode_uri, vscode_dir)

    print('Creating data folder...', end='')
    if not os.path.exists('vscode/data'):
        os.makedirs('vscode/data')
    print('Done')

    print('VSCode installed to ' + vscode_dir)

def install_vscode_extensions():
    vscode_path = os.path.join(pdev_dir, 'vscode\\code.exe')
    if not os.path.exists(vscode_path):
        print('VSCode not installed')
        return

    print('Installing VSCode extensions')
    with urllib.request.urlopen(vscode_extension_list_uri) as response:
        data = response.read()
        text = data.decode('utf-8')
        
        extensions = text.split('\n')
        
        for ext in extensions:
            vscode_path = os.path.join(pdev_dir, 'vscode\\bin\\code.cmd')
            vscode_cmd = [vscode_path, '--install-extension', ext]
            subprocess.call(vscode_cmd)

def install_vscode_settings():
    vscode_path = os.path.join(pdev_dir, 'vscode\\code.exe')
    if not os.path.exists(vscode_path):
        print('VSCode not installed')
        return

    print('Installing VSCode settings')
    with urllib.request.urlopen(vscode_user_settings_uri) as response:
        data = response.read()
        text = data.decode('utf-8')

        vscode_settings_path = os.path.join(pdev_dir, 'vscode\\data\\user-data\\User')
        if not os.path.exists(vscode_settings_path):
            os.makedirs(vscode_settings_path)
        
        with open(os.path.join(vscode_settings_path, 'settings.json'), 'w') as _file:
            _file.write(text)

def install_tools(tools=None):
    if 'all' in tools:
        print('Installing full pDev environment...')
        install_vscode()
        print('Done')
    else:
        if 'vscode' in tools:
            install_vscode()
        if 'vscode_ext' in tools:
            install_vscode_extensions()
        if 'vscode_settings' in tools:
            install_vscode_settings()
        if 'rust' in tools:
            print('rust install not supported')
            # install_rust()
        if 'node' in tools:
            print('node install not supported')
            # install_node()
        if 'yarn' in tools:
            print('yarn install not supported')
            # install_yarn()

def run_vscode():
    if platform == 'linux' or platform == 'linux2':
        print('Running vscode for linux not supported yet :(')
    elif platform == 'darwin':
        print('Running vscode for macOS not supported yet :(')
    elif platform == 'win32':
        vscode_path = os.path.join(pdev_dir, 'vscode\\code.exe')
        if os.path.exists(vscode_path):
            os.execl(vscode_path, " ")
        else:
            print('VSCode not installed')

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

parser.add_argument('command', nargs='?', help='Command to run')

# parser.add_argument('alias', nargs='?', help='Creates a \'pdev\' alias for your terminal.')
# parser.add_argument('code', nargs='?', help='Opens VSCode')

args = parser.parse_args()

if args.install is not None:
    install_tools(args.install)
if args.command == 'alias':
    add_alias()
if args.command == 'code':
    run_vscode()
