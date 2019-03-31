from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

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
		#Returns the URL where the contents of the file referenced by name can be accessed.
        uploaded_file_url = fs.url(filename)
		#this will redirct us to the dash_app
        redirectURL = '/dash_results/'
    return render(request, 'upload.html',{
	  'uploaded_file_url': uploaded_file_url,
	  'redirectURL': redirectURL
	})
#this renders the about.html page
def about(request):
    return render(request, 'about.html')

#renders the contact.html page
def contact(request):
	return render(request, 'contact.html')
