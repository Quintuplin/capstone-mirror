from pyteomics import mzml, auxiliary
import pymzml as pyM
import csv
with mzml.read('/home/cowdendt/Desktop/NIST/capstone-2019-nist/capstone/upload/0.mzML') as reader:
	auxiliary.print_tree(next(reader))


#reference_file = 'lala.mzML'
reference_file = pyM.run.Reader("/home/cowdendt/Desktop/NIST/capstone-2019-nist/capstone/upload/lala.mzML")
amount_injected = 200
fasta_file = '/home/cowdendt/Desktop/NIST/capstone-2019-nist/capstone/upload/up000005640.fasta'
spectrast_library = 'HeLa.splib'
query = '0'
query_file = pyM.run.Reader('/home/cowdendt/Desktop/NIST/capstone-2019-nist/capstone/upload/0.mzML')


#reference_file <- openMSfile(paste(REFERENCE, '.mzML', sep=''))
with open("ref.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',
						quotechar=' ',quoting=csv.QUOTE_MINIMAL)
	#ref_list = []
	writer.writerow(['','Time','TIC', 'Sample'])
	n = 0
	for spectrum in reference_file:
		ref_time = spectrum.scan_time
		ref_tic = spectrum.TIC
		writer.writerow([n, ref_time[0],ref_tic,'HeLa'])
		n+=1
		#ref_list = ref_list+ref_tic

with open("que.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',
						quotechar=' ',quoting=csv.QUOTE_MINIMAL)

	writer.writerow(['','Time','TIC', 'Sample'])
	n = 0
	for spectrum in query_file:
		q_time = spectrum.scan_time
		q_tic = spectrum.TIC
		writer.writerow([n,q_time[0],q_tic,'HeLa'])
		n+=1
		#writer.write("\n")
		#print("reference TIC: ", ref_tic)

	#for spectrum in query_file:
	#	q_tic = spectrum.TIC
	#print("query TIC:", q_tic)


	#f.write(str(q_tic))
	#f.close()
	#writer.close()
