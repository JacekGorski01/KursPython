import os
from send2trash import send2trash

os.mknod("plik.txt")
send2trash('plik.txt')
