$python3_uri = 'https://www.python.org/ftp/python/3.6.5/python-3.6.5-embed-amd64.zip'
$pdev_python_installer_uri = ''
$tools = 'all'

# Set TSL protocol to version 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Unzips .zip files
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip {
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}

# Download python
try {
    Invoke-WebRequest -Uri $python3_uri -OutFile python.zip
} catch {
    "Failed to download python from: $python3_uri"
    exit
}

# Store portable python to 'python' directory
mkdir python
Unzip python.zip python

# Remove zipped python file
del python.zip

# Pass control to cross-platform installer
.\python\python.exe pdev.py --install $tools