import os
import urllib
import subprocess
import pdev_tools.util as util
from sys import platform

class PDevTool_Rust():
    _rust_windows_uri = 'https://win.rustup.rs'

    def __init__(self):
        self.name = 'Rust'
        self.cli_name = 'rust'
    
    def install(self, dir):
        if self.is_installed(dir):
            print('Rust already installed')
            return
        
        print('Installing rust...')
        if platform == 'linux' or platform == 'linux2':
            print('Rust installation not supported for linux yet :(')
        elif platform == 'darwin':
            print('Rust installation not supported for macOS yet :(')
        elif platform == 'win32':
            rust_path = os.path.join(dir, 'rustup-init.exe')
            util.download_file(PDevTool_Rust._rust_windows_uri, rust_path)
            if subprocess.call(rust_path) != 0:
                print('Rust installation failed?')
            else:
                print('Done')
    
    def is_installed(self, dir):
        try:
            subprocess.call('rustup -V')
            return True
        except:
            return False

    def init_argparser(self, parser):
        parser.add_parser('rust', help='Rust commands')

    def parse_args(self, args, dir):
        if args.toolcmd == 'rust':
            if not self.is_installed(dir):
                print('Rust not installed')
                return
        return

def __init_tool():
    return PDevTool_Rust()