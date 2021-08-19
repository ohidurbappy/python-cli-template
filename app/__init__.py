import os
import sys


def print_system_info():
    print("** System Info **")
    print("OS:", os.name.capitalize())
    print("Platform: ",sys.platform)
    print("Current Dir: ",os.curdir)
    print("Python: %d.%d"%(sys.version_info.major,sys.version_info.minor))
