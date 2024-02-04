# https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on/58071295#58071295
import platform
import wget
import os

url = None
filename = None

# macOS
if platform.system().lower() == 'darwin':
    url = None
    # TODO : GET URL

elif platform.system().lower() == 'windows':
    url = 'http://files.mcneel.com/yak/tools/latest/yak.exe'
    filename = 'yak.exe'

else:
    print("Unsupported OS Used!")
    exit(1)

if os.path.isfile(filename):
    print('Yak is already downloaded. Using Cached version.')
    exit(0)

if filename is None or url is None:
    print("An unexpected error occured. Could not obtain Yak Info")
    exit(2)

wget.download(url, filename)
