import sys
import os

if os.path.isfile('yak.exe'):
    print('Yak is already downloaded. Using Cached version')
    sys.exit(0)

try:
    import wget
    url = 'http://files.mcneel.com/yak/tools/latest/yak.exe'
    wget.download(url, 'yak.exe')

    sys.exit(0)

except:
    import sys
    print ('failed to download yak from McNeel Servers')
    sys.exit(1)
