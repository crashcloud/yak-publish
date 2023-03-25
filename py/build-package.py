import subprocess as proc
from glob import glob
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--platform", type=str, default='any', choices=['win', 'mac', 'windows-latest', 'macos-latest', 'any'])
parser.add_argument("-b", "--buildpath", type=str, required=True)

args = parser.parse_args()

platform = args.platform[:3].lower()

cwd = os.getcwd()
yak_exe_path = f'{cwd}\yak.exe'

for dir in glob(args.buildpath):
    os.chdir(dir)
    print(f'moved to {os.getcwd()}')

    proc.run( [ yak_exe_path, 'build', '--platform', platform ] )

os.chdir(cwd)
sys.exit(0)