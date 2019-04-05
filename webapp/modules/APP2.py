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
                if name.split('.')[-1] != "raw":
                    found = True
            for name in dirs:
                print (name)
    #temp dummy filegen so it returns true on second call
    completeName = os.path.join(basePath, str(ID), "report.csv")    

    file1 = open(completeName, "w")
    images = ["green", "orange", "red"]
    subpages = ["sampleimage", "lcimage", "sourceimage", "ms1image", "ms2image"]
    for subpage in subpages:
        sample = "{% static 'img/" + str(images[random.randint(0,2)]) +".jpg' %}"
        print(subpage + ";" + sample + "\n")
        file1.write(subpage + ";" + sample + "\n")
    file1.close()

    return found