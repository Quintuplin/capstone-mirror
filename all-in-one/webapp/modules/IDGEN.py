import os
import string
import random

ALLOWED_EXTENSIONS = set(['raw', 'mzML'])

def IDgen(basePath):
    idlen = 10
    collisions = 0
    ID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(idlen)) #generate ID
    while os.path.exists(os.path.join(basePath, str(ID))):
        collisions += 1
        if collisions >= 10:
            collisions = 0
            idlen = idlen + 1
        ID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(idlen)) #generate new ID
    print(ID)
    return str(ID)

def DIRgen(basePath):
    ID = IDgen(basePath)
    DIR = os.path.join(basePath, ID)
    os.mkdir(DIR)
    print(DIR)
    return DIR

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS