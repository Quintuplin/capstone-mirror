import os

def DIRcheck(ID, basePath):
    if os.path.exists(os.path.join(basePath, str(ID))):
        return os.path.join(basePath, str(ID))
    else:
        return -1