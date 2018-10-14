$directory_path = $HOME + "\pdev"
$pdev_exec_path = $directory_path + "\pdev.py"
$python_zip_path = $directory_path + "\python.zip"
$python_install_dir = $directory_path + "\python"
$python_exe_path = $python_install_dir + "\python.exe"
$python3_uri = 'https://www.python.org/ftp/python/3.6.5/python-3.6.5-embed-amd64.zip'
$pdev_uri = 'https://raw.githubusercontent.com/pcleavelin/pDev/master/pdev.py'
$tools = 'all'
$pdev_run_cmd = "$python_exe_path $pdev_exec_path --install $tools -alias"

# Set TSL protocol to version 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Unzips .zip files
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip {
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}

# Create pDev directory
mkdir $directory_path

# Download pDev
try {
    Invoke-WebRequest -Uri $pdev_uri -OutFile $pdev_exec_path
} catch {
    "Failed to download pDev script from: $pdev_uri"
    exit
}

# Download python
try {
    Invoke-WebRequest -Uri $python3_uri -OutFile $python_zip_path
} catch {
    "Failed to download python from: $python3_uri"
    exit
}

# Store portable python to 'python' directory
try {
    mkdir $python_install_dir
} finally {
    Unzip $python_zip_path $python_install_dir
}

# Remove zipped python file
Remove-Item $python_zip_path

# Pass control to cross-platform installer
cd $directory_path
Invoke-Expression $pdev_run_cmd