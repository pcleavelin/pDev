import os
import urllib.request
import shutil
import zipfile
from argparse import ArgumentParser

# pDev Tools
vscode_uri = 'https://go.microsoft.com/fwlink/?Linkid=850641'
vscode_extension_list_uri = '<insert github link here>'
rust_uri = '<insert rust curl url here>'

def download_extract_zip(uri, out_path):
    print('Downloading...')
    with urllib.request.urlopen(uri) as response, open('tmp.zip', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    # Make sure to create directory first if it doesn't already exists
    if not os.path.exists(out_file):
        os.makedirs(out_file)

    print('Extracting to directory...', end='')
    with zipfile.ZipFile('tmp.zip', 'r') as zip_ref:
        zip_ref.extractall(out_path)
    
    if os.path.exists('tmp.zip'):
        os.remove('tmp.zip')
    print('Done')

def install_vscode():
    download_extract_zip(vscode_uri, 'vscode')

    print('Creating data folder...', end='')
    if not os.path.exists('vscode/data'):
        os.makedirs('vscode/data')
    print('Done')

    vscode_dir = os.path.join(os.path.abspath(os.path.curdir), 'vscode')
    print('VSCode installed to ' + vscode_dir)

def install_tools(tools=None):
    if tools is None:
        print('Installing full pDev environment...')
        install_vscode()
    else:
        if 'vscode' in tools:
            install_vscode()
        # if 'rust' in tools:
        #     install_rust()
        # if 'node' in tools:
        #     install_node()
        # if 'yarn' in tools:
        #     install_yarn()

def tool_list(string):
    values = string.split(',')
    return values

parser = ArgumentParser(description='The pDev environment')
parser.add_argument('--install', metavar='TOOLS', type=tool_list, help='List of tools to install. \'--install all\' for full installation')

args = parser.parse_args()

if args.install is not None:
    install_tools(args.install)
