#!/usr/bin/env python3


import os
from datetime import date
import stat
for ent in os.scandir():
    if ent.is_dir():
        print("{} is a dir".format(ent.name))
    if ent.is_file():
        print("{} is a file".format(ent.name))
    # get file information
    stats = os.stat(ent.path)
    print("fperm: {}".format(stat.filemode(stats.st_mode)))
    atime, mtime, ctime = date.fromtimestamp(stats.st_atime), date.fromtimestamp(stats.st_mtime), date.fromtimestamp(stats.st_ctime)
    print("Access: {} \t Mod: {} \t Creat: {}".format(atime, mtime, ctime))