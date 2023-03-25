import subprocess as proc
from glob import glob
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--publish", type=str, default=' ', choices=[None, 'test', 'production'])
parser.add_argument("-b", "--buildpath", type=str, required=True)

args = parser.parse_args()

source = None
if args.publish == 'test':
    source="https://test.yak.rhino3d.com"
if args.publish == 'production':
    source="https://yak.rhino3d.com"

if source == None:
    print ('Publish is None, exiting.')
    sys.exit(0)

cwd = os.getcwd()
yak_exe_path = f'{cwd}\yak.exe'

yakPackages = glob(f'{args.buildpath}\*.yak')
if yakPackages:
    for yakPackage in yakPackages:
        proc.run( [ yak_exe_path, 'push', yakPackage, '--source', source ] )
        print (f'Published package {yakPackage} successfully to {source}')
else:
    print (f'No Yak Packages found for given build path {args.buildpath}')
    sys.exit(1)

sys.exit(0)