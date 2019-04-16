from pyteomics import mzml, auxiliary
import pymzml as pyM
import csv
with mzml.read('0.mzML') as reader:
	auxiliary.print_tree(next(reader))


#reference_file = 'lala.mzML'
reference_file = pyM.run.Reader("lala.mzML")
amount_injected = 200
fasta_file = 'up000005640.fasta'
spectrast_library = 'HeLa.splib'
query = '0'
query_file = pyM.run.Reader('0.mzML')


#reference_file <- openMSfile(paste(REFERENCE, '.mzML', sep=''))
with open("ref.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',
						quotechar=' ',quoting=csv.QUOTE_MINIMAL)
	#ref_list = []
	writer.writerow(['','TIC', 'Time','Sample'])
	n = 0
	for spectrum in reference_file:
		ref_tic = spectrum.TIC
		ref_time = spectrum.scan_time
		writer.writerow([n,ref_tic, ref_time[0],'HeLa'])
		n+=1
		#ref_list = ref_list+ref_tic

with open("que.csv", "w", newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',
						quotechar=' ',quoting=csv.QUOTE_MINIMAL)

	writer.writerow(['','TIC', 'Time','Sample'])
	n = 0
	for spectrum in query_file:
		q_tic = spectrum.TIC
		q_time = spectrum.scan_time
		writer.writerow([n, q_tic, q_time[0],'HeLa'])
		n+=1
		#writer.write("\n")
		#print("reference TIC: ", ref_tic)

	#for spectrum in query_file:
	#	q_tic = spectrum.TIC
	#print("query TIC:", q_tic)


	#f.write(str(q_tic))
	#f.close()
	#writer.close()
