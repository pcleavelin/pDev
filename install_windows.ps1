$innvocation = (Get-Variable MyInvocation).Value
$directory_path = Split-Path $innvocation.MyCommand.Path
$python_zip_dir = $directory_path + "\python.zip"
$python_install_dir = $directory_path + "\python"
$python_exe_dir = $python_install_dir + "\python.exe"
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
try {
    mkdir python
} finally {
    Unzip $python_zip_dir $python_install_dir
}

# Remove zipped python file
Remove-Item "python.zip"

# Pass control to cross-platform installer
.\python\python.exe pdev.py --install $tools