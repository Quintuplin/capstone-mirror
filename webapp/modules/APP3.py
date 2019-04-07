import os
import random
from shutil import copyfile

def RESULTgen(ID, basePath, staticPath):
    found = False
    if os.path.exists(os.path.join(basePath, str(ID))):
        print("Path Found")
        for root, dirs, files in os.walk(os.path.join(basePath, str(ID)), topdown=False):
            print("Checking Contents in: " + root)
            for name in files:
                print (name)
                if name.split('.')[-1] == "raw":
                    found = True
            for name in dirs:
                print (name)

    completeName = os.path.join(basePath, str(ID), "report.csv")    
    doneName = os.path.join(basePath, str(ID), "app3.done")    

    if found:
        #this is the dummy graph output command
        #when APP3 is imported from v1, the 'g1.jpg' file will instead be directly generated into the results folder
        copyfile(os.path.join(staticPath, "img", "line.jpg"), os.path.join(basePath, str(ID), "g1.jpg"))

        file1 = open(completeName, "w")
        images = ["green", "orange", "red"]
        subpages = ["sampleimage", "lcimage", "sourceimage", "ms1image", "ms2image"]
        for subpage in subpages:
            sample = "{% static 'img/" + str(images[random.randint(0,2)]) +".jpg' %}"
            print(subpage + ";" + sample + "\n")
            file1.write(subpage + ";" + sample + "\n")
        file1.close()

        file2 = open(doneName, "w")
        file2.write("Report Generated\n")
        file2.close()
    return found