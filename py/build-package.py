import subprocess as proc
from pathlib import Path
from glob import glob
import platform
import argparse
import shutil
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buildpath", type=str, required=True)
parser.add_argument("-v", "--version", type=int, required=True, choices=[7, 8], help='Rhino Version to build for')

args = parser.parse_args()

curr_platform = None
yak_filename = None

# macOS
if platform.system().lower() == 'darwin':
    curr_platform = 'mac'
    yak_filename = 'yak'

elif platform.system().lower() == 'windows':
    curr_platform = 'win'
    yak_filename = 'yak.exe'

else:
    print("Unsupported OS Used!")
    exit(1)

cwd = os.getcwd()
yak_exe_path = f'{cwd}\{yak_filename}'

def get_yak_resources() -> (str, str, list):
    manifest = None
    icon = None
    yaks = []

    for file in os.listdir():
        if file.lower() == 'manifest.yaml' or file.lower() == 'manifest.yml':
            manifest = file

        elif file.lower() == 'icon.png':
            icon = file

        elif file.endswith('.yak'):
            yaks.append(file)
            
    return (manifest, icon, yaks)

def delete_yak_resources():
    child_dirs = glob(f'{os.cwd()}\**\\')
    for dir in child_dirs:
        for file in os.listdir(dir):
            if file.lower() == 'manifest.yaml' or file.lower() == 'manifest.yml':
                Path(file).unlink()

            elif file.lower() == 'icon.png':
                Path(file).unlink()
            
            elif file.lower().endswith('.yak'):
                Path(file).unlink()

for dir in glob(args.buildpath):
    os.chdir(dir)
    print(f'moved to {os.getcwd()}')

    if args.version <= 7:
        proc.run( [ yak_exe_path, 'build', '--platform', curr_platform ] )

    # TODO : What if User feeds in directory that has net48/net7.0 below it?
    elif args.version >= 8:
        (manifest, icon, yaks) = get_yak_resources()

        up_dir = Path(os.getcwd()).parent.absolute()

        for yak in yaks:
            shutil.copy(yak, up_dir)

        # Copy manifest / Icon up 1 level (if they exist)
        if manifest is not None:
            shutil.copy(manifest, up_dir)
        if icon is not None:
            shutil.copy(icon, up_dir)

        # Move up 1 level
        os.chdir(up_dir)

        # Delete EVERY manifest / Icon 1 level below
        delete_yak_resources()

        # Run Build
        proc.run( [ yak_exe_path, 'build', '--platform', curr_platform ] )

    else:
        print ("An Unknown Scenario occured")
        exit (2)

os.chdir(cwd)
sys.exit(0)
