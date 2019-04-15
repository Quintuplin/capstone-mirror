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

    completeName = os.path.join(basePath, str(ID), "report.txt")    
    doneName = os.path.join(basePath, str(ID), "app3.done")    

    if found:
        #this is the dummy graph output command
        #when APP3 is imported from v1, the 'g1.jpg' file will instead be directly generated into the results folder
        
        #img dummy
        copyfile(os.path.join(staticPath, "img", "line.jpg"), os.path.join(basePath, str(ID), "g1.jpg"))

        #graph dummy
        file2a = open(os.path.join(staticPath, "sample.csv"), "r")
        file2b = open(os.path.join(basePath, str(ID), "results1.csv"), "w")
        for line in file2a:
            file2b.write(line)

        file1 = open(completeName, "w")
        images = ["green", "orange", "red"]
        subpages = ["sampleimage", "lcimage", "sourceimage", "ms1image", "ms2image"]
        for subpage in subpages:
            sample =str(images[random.randint(0,2)])
            print(subpage + " " + sample + "\n")
            file1.write(subpage + " " + sample + "\n")
        file1.close()

        file3 = open(doneName, "w")
        file3.write("Report Generated\n")
        file3.close()
    return found