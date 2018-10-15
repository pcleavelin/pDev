import os
import urllib
import shutil
import zipfile

class ToolCommand():
    def __init__(self, name, description):
        self.name = name
        self.description = description

def download_file(uri, out_path):
    print('Downloading...')
    with urllib.request.urlopen(uri) as response, open(out_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def download_extract_zip(uri, out_path):
    downloads_dir = os.path.join(os.path.expanduser('~'), "Downloads")
    tmp_zip = os.path.join(downloads_dir, 'tmp.zip')
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