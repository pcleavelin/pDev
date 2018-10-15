import os
import urllib
import subprocess
import pdev_tools.util as util
from sys import platform

class PDevTool_VSCode():
    _vscode_uri = 'https://go.microsoft.com/fwlink/?Linkid=850641'
    _vscode_extension_list_uri = 'https://gist.githubusercontent.com/pcleavelin/8d08dd2436aedc67f43615c1a1600da6/raw/9aa91fb16b50d31955667c479ca3df917885bf55/VSCode_Extensions.txt'
    _vscode_user_settings_uri = 'https://gist.githubusercontent.com/pcleavelin/8d08dd2436aedc67f43615c1a1600da6/raw/9aa91fb16b50d31955667c479ca3df917885bf55/VSCode_Settings.json'

    def __init__(self):
        self.name = 'VSCode'
        self.path = 'vscode'
    
    def install(self, dir):
        print('Installing VSCode...')
        vscode_dir = os.path.join(dir, 'vscode')

        util.download_extract_zip(PDevTool_VSCode._vscode_uri, vscode_dir)

        print('Creating data folder...', end='')
        data_dir = os.path.join(vscode_dir, 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        print('Done')

        print('VSCode installed to ' + vscode_dir)

    def install_extensions(self, dir):
        # Should probably look for executable file, but whatever
        vscode_path = os.path.join(dir, 'vscode')
        if not os.path.exists(vscode_path):
            print('VSCode not installed')
            return

        print('Installing VSCode extensions')
        with urllib.request.urlopen(PDevTool_VSCode._vscode_extension_list_uri) as response:
            data = response.read()
            text = data.decode('utf-8')
            
            extensions = text.split('\n')
            
            for ext in extensions:
                # Might not work in linux and macOS
                vscode_path = os.path.join(dir, 'vscode\\bin\\code.cmd')
                vscode_cmd = [vscode_path, '--install-extension', ext]
                subprocess.call(vscode_cmd)
        print('Done')

    def install_settings(self, dir):
        # Should probably look for executable file, but whatever
        vscode_path = os.path.join(dir, 'vscode')
        if not os.path.exists(vscode_path):
            print('VSCode not installed')
            return

        print('Installing VSCode settings')
        with urllib.request.urlopen(PDevTool_VSCode._vscode_user_settings_uri) as response:
            data = response.read()
            text = data.decode('utf-8')

            vscode_settings_path = os.path.join(dir, 'vscode\\data\\user-data\\User')
            if not os.path.exists(vscode_settings_path):
                os.makedirs(vscode_settings_path)
            
            with open(os.path.join(vscode_settings_path, 'settings.json'), 'w') as _file:
                _file.write(text)
            print('Installed settings to '+ vscode_settings_path)
        
    def open(self, dir):
        if platform == 'linux' or platform == 'linux2':
            print('Running vscode for linux not supported yet :(')
        elif platform == 'darwin':
            print('Running vscode for macOS not supported yet :(')
        elif platform == 'win32':
            vscode_path = os.path.join(dir, 'vscode\\code.exe')
            if os.path.exists(vscode_path):
                os.execl(vscode_path, " ")
            else:
                print('VSCode not installed')

    def init_argparser(self, parser):
        code_parser = parser.add_parser('code', help='VSCode commands')
        code_parser.add_argument('--install-ext', action='store_true', help='Install VSCode extensions')
        code_parser.add_argument('--install-settings', action='store_true', help='Install VSCode user settings')

    def parse_args(self, args, dir):
        if args.toolcmd == 'code':
            if args.install_ext:
                self.install_extensions(dir)
            elif args.install_settings:
                self.install_settings(dir)
            else:
                self.open(dir)

def __init_tool():
    return PDevTool_VSCode()