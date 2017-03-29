#import os.path

#if  os.path.exists(file_name)==True: print("I get the file >hubaa")

#if os.path.exists(file_name)==False:
#      print("The File s% it's not created "%file_name)
#      os.touch(file_name)
#      print("The file s% has been Created ..."%file_name)

from os import path

strPath = r"/home/Document/Python/i3status"

print("the current directoryis: %s" % strPath)
print("abspath = %s" % path.abspath(strPath))
print("dirname = %s" % path.dirname(strPath))
print("basename = %s" % path.basename(strPath))
print("exists = %s" % path.exists(strPath))
print("isdir = %s" % path.isdir(strPath))
print("isfile = %s" % path.isfile(strPath))
