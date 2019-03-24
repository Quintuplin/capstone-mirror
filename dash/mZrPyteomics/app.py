import matplotlib.pyplot as plt
import numpy
import pyteomics.mzml
import pyteomics.fasta

MZFILE = "/project/app_uploaded_files/2018-11-5_HeLa_OTOT1111.mzML"
FASTAFILE = "/project/app_uploaded_files/up000005640.fasta"

j = 0

print ("mzml read")
print (pyteomics.mzml.version_info(MZFILE))
data = pyteomics.mzml.read(MZFILE)
for result in data:
   print (result)
   j+=1
   if (j > 10):
      break
print ("mzml done")

print ("FASTA read")
data = pyteomics.fasta.read(FASTAFILE)
for result in data:
   print (result)
   j+=1
   if (j > 20):
      break
print ("FASTA done")
