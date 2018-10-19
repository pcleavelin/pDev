import os
import urllib
import subprocess
import pdev_tools.util as util
from sys import platform

class PDevTool_Sublime():
    _sublime_windows_uri = 'https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip'

    def __init__(self):
        self.name = 'Sublime'
        self.cli_name = 'sublime'
    
    def install(self, dir):
        if self.is_installed(dir):
            print('Sublime already installed')
            return
        
        print('Installing sublime...')
        if platform == 'linux' or platform == 'linux2':
            print('Sublime installation not supported for linux yet :(')
        elif platform == 'darwin':
            print('Sublime installation not supported for macOS yet :(')
        elif platform == 'win32':
            sublime_dir = os.path.join(dir, 'sublime')
            util.download_extract_zip(PDevTool_Sublime._sublime_windows_uri, sublime_dir)
    
    def is_installed(self, dir):
        # Should probably look for executable file, but whatever
        sublime_dir = os.path.join(dir, 'sublime')
        if not os.path.exists(sublime_dir):
            return False
        return True

    def open(self, dir):
        if platform == 'linux' or platform == 'linux2':
            print('Running vscode for linux not supported yet :(')
        elif platform == 'darwin':
            print('Running vscode for macOS not supported yet :(')
        elif platform == 'win32':
            sublime_path = os.path.join(dir, 'sublime\\sublime_text.exe')
            if os.path.exists(sublime_path):
                os.execl(sublime_path, " ")
            else:
                print('Sublime not installed')

    def init_argparser(self, parser):
        parser.add_parser('sublime', help='Sublime commands')

    def parse_args(self, args, dir):
        if args.toolcmd == 'sublime':
            if not self.is_installed(dir):
                print('Sublime not installed')
                return

            self.open(dir)
        return

def __init_tool():
    return PDevTool_Sublime()