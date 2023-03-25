import subprocess as proc
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--platform", type=str, default='any', choices=['win', 'mac', 'any'])
parser.add_argument("-b", "--buildpath", type=str, required=True)

args = parser.parse_args()

platform = args.platform[:3].lower()

cwd = os.getcwd()
yak_exe_path = f'{cwd}\yak.exe'


os.chdir(args.buildpath)
print(f'moved to {os.getcwd()}')

try:
    result = proc.run( [ yak_exe_path, 'build', '--platform', platform ] )
    if (result.returncode == 1):
        print ('yak failed to build')
finally:
    os.chdir(cwd)

sys.exit(result.returncode)