import os
import random

def DIRcheck(ID, basePath):
    if os.path.exists(os.path.join(basePath, str(ID))):
        return os.path.join(basePath, str(ID))
    else:
        return -1

def RESULTcheck(ID, basePath):
    found = False
    if os.path.exists(os.path.join(basePath, str(ID))):
        print("Path Found")
        for root, dirs, files in os.walk(os.path.join(basePath, str(ID)), topdown=False):
            print("Checking Contents in: " + root)
            for name in files:
                print (name)
                if name.split('.')[-1] == "done":
                    found = True
            for name in dirs:
                print (name)
    return found