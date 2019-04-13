from pyteomics import mzml, auxiliary
import pymzml as pyM
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
for spectrum in reference_file:
	ref_tic = spectrum.TIC
print("reference TIC: ", ref_tic)

for spectrum in query_file:
	q_tic = spectrum.TIC
print("query TIC:", q_tic)

f = open("test.txt", "w")
f.write(str(ref_tic))
f.write("\n")
f.write(str(q_tic))
f.close()
#output$TICplot <- renderPlot({
#      plot(query_TIC[,1], query_TIC[,2], type="h", lwd=1, col='green', xlab='retention time (min)', ylab='total ion current')
#      lines(reference_TIC[,1], reference_TIC[,2], type="h", lwd=1, col='blue')
#})
