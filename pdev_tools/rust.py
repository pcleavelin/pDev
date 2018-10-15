import os
import urllib
import subprocess
import pdev_tools.util as util
from sys import platform

class PDevTool_Rust():
    _rust_windows_uri = 'https://win.rustup.rs'

    def __init__(self):
        self.name = 'Rust'
    
    def install(self, dir):
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

    def init_argparser(self, parser):
        parser.add_parser('rust', help='Rust commands')

    def parse_args(self, args, dir):
        return

def __init_tool():
    return PDevTool_Rust()