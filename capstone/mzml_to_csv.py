from pyteomics import mzml, auxiliary
import pymzml as pyM
import csv
from upload.views import upload_file as upload
import os
import sys
import string as str

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#grab the argument passed from views.py

#grab 1st index to get filename
argument = sys.argv[1]
print(argument)

#replace filename.raw with filename.mzml in order to find the mzml file
mzml_file = argument.replace('.RAW', '.mzML')
print(mzml_file)
mzml_file_location = BASE_DIR +'/capstone/uploads/'+mzml_file

#naviagates to the files needed
query_file = BASE_DIR + '/capstone/uploads/references/0.mzML'
hela_file = BASE_DIR + '/capstone/uploads/references/HeLa.splib'

reference_file = pyM.run.Reader(mzml_file_location)
amount_injected = 200

spectrast_library = hela_file
query = '0'

query_file = pyM.run.Reader(query_file)


#reference_file <- openMSfile(paste(REFERENCE, '.mzML', sep=''))
with open("ref.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=' ',
						quotechar=' ',quoting=csv.QUOTE_MINIMAL)

	n = 0
	for spectrum in reference_file:
		ref_tic = spectrum.TIC
		ref_time = spectrum.scan_time
		writer.writerow([n,ref_tic, ref_time[0],'HeLa'])
		n=n+1
		#ref_list = ref_list+ref_tic

with open("que.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=' ',
						quotechar=' ',quoting=csv.QUOTE_MINIMAL)
	for spectrum in query_file:
		q_tic = spectrum.TIC
		q_time = spectrum.scan_time
		writer.writerow([q_tic, q_time[0],'HeLa'])
		#writer.write("\n")
		#print("reference TIC: ", ref_tic)

	#for spectrum in query_file:
	#	q_tic = spectrum.TIC
	#print("query TIC:", q_tic)


	#f.write(str(q_tic))
	#f.close()
	#writer.close()
os.remove(mzml_file_location)