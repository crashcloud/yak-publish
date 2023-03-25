import sys
import os

if os.path.isfile('yak.exe'):
    print('Yak is already downloaded. Using Cached version')
    sys.exit(0)

import wget
url = 'http://files.mcneel.com/yak/tools/latest/yak.exe'
wget.download(url, 'yak.exe')
