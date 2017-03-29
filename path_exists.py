#from os import path

#strPath = r"/home/Document/Python/i3status"

#print("the current directoryis: %s" % strPath)
#print("abspath = %s" % path.abspath(strPath))
#print("dirname = %s" % path.dirname(strPath))
#print("basename = %s" % path.basename(strPath))
#print("exists = %s" % path.exists(strPath))
#print("isdir = %s" % path.isdir(strPath))
#print("isfile = %s" % path.isfile(strPath))


#import os.path


#def pathExists(strPath):
#    if os.path.exists(strPath):
#        print ("True")
#        print("exists = %s" % path.exists(strPath))
#        print("isdir = %s" % path.isdir(strPath))
#        print("isfile = %s" % path.isfile(strPath))


import os.path

strPath = r"/home"

if os.path.exists(strPath):
    print ("True")

