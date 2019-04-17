from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import subprocess as sub
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

#this method was retrieved from stack overflow on 3.14.19
def upload_file(request):
	#if we have post requesst
    if request.method == 'POST':

		#assign a variable the responsibility of the file
        myfile = request.FILES['myfile']

		#get file system variable, documentation on FileSystemStorage: https://docs.djangoproject.com/en/2.1/ref/files/storage/
        fs = FileSystemStorage()

		#gsave the file to the file system that you have set up
        filename = fs.save(myfile.name, myfile)
		#give the file a custome URL
        print(filename)
        #referenced by name can be accessed.
        uploaded_file_url = BASE_DIR + fs.url(filename)
        #print(uploaded_file_url)

		#this will redirct us to the dash_app
        redirectURL = '/dash_results/'
        uploaded_file = '/data/'+ filename
        file_location = BASE_DIR + '/uploads:/data'
        # hard coded path should be changed

        sub.run(['docker', 'run', '-it', '--rm', '-e', 'WINEDEBUG=-all', '-v',
                        file_location,
                        'chambm/pwiz-skyline-i-agree-to-the-vendor-licenses', 'wine', 'msconvert',
                        uploaded_file])

        print('docker subprocess complete')
        script_location =BASE_DIR + '/mzml_to_csv.py'
        sub.run(['python3', script_location, filename])


        print('python3 subprocess complete')
        os.remove(uploaded_file_url)
        #render the upload.html file and pass the url for the file and the url to redirect
        return render(request, 'upload.html', {
            'uploaded_file': uploaded_file,
            'redirectURL': redirectURL
        })
    return render(request, 'upload.html')

def about(request):

    return render(request, 'about.html')


def contact(request):

	return render(request, 'contact.html')
