import os

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
            print("Checking Contents")
            for name in files:
                print (name)
                if name.split('.')[-1] != "raw":
                    found = True
            for name in dirs:
                print (name)
    #temp dummy filegen so it returns true on second call
    completeName = os.path.join(basePath, str(ID), "report.csv")         
    file1 = open(completeName, "w")
    file1.write("Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin\n")
    file1.write("STRING;DOUBLE;INT;DOUBLE;DOUBLE;DOUBLE;DOUBLE;INT;CAT\n")
    file1.write("Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US\n")
    file1.write("Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US\n")
    file1.write("Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US\n")
    file1.close()

    return found