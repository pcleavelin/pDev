import os
import urllib
import subprocess
import pdev_tools.util as util
from sys import platform

class PDevTool_SublimeMerge():
    _sublime_merge_windows_uri = 'https://download.sublimetext.com/sublime_merge_build_1075_x64.zip'

    def __init__(self):
        self.name = 'Sublime Merge'
        self.cli_name = 'sbmerge'
    
    def install(self, dir):
        if self.is_installed(dir):
            print('Sublime Merge already installed')
            return
        
        print('Installing sublime merge...')
        if platform == 'linux' or platform == 'linux2':
            print('Sublime installation not supported for linux yet :(')
        elif platform == 'darwin':
            print('Sublime installation not supported for macOS yet :(')
        elif platform == 'win32':
            sublime_merge_dir = os.path.join(dir, 'sublime_merge')
            util.download_extract_zip(PDevTool_SublimeMerge._sublime_merge_windows_uri, sublime_merge_dir)
    
    def is_installed(self, dir):
        # Should probably look for executable file, but whatever
        sublime_merge_dir = os.path.join(dir, 'sublime_merge')
        if not os.path.exists(sublime_merge_dir):
            return False
        return True

    def open(self, dir):
        if platform == 'linux' or platform == 'linux2':
            print('Running vscode for linux not supported yet :(')
        elif platform == 'darwin':
            print('Running vscode for macOS not supported yet :(')
        elif platform == 'win32':
            sublime_merge_path = os.path.join(dir, 'sublime_merge\\sublime_merge.exe')
            if os.path.exists(sublime_merge_path):
                os.execl(sublime_merge_path, " ")
            else:
                print('Sublime Merge not installed')

    def init_argparser(self, parser):
        parser.add_parser('sbmerge', help='Sublime Merge commands')

    def parse_args(self, args, dir):
        if args.toolcmd == 'sbmerge':
            if not self.is_installed(dir):
                print('Sublime Merged not installed')
                return

            self.open(dir)
        return

def __init_tool():
    return PDevTool_SublimeMerge()