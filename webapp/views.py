from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.urls import path

from .modules.APP1 import DIRgen, allowed_file
from .modules.APP2 import DIRcheck
from capstone.settings import MEDIA_ROOT

#this method was retrieved from stack overflow on 3.14.19
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        if allowed_file(myfile.name):
            ID, DIR = DIRgen(MEDIA_ROOT)
            fs = FileSystemStorage(location=DIR)
            fs.save(myfile.name, myfile)
            uploaded_file_url = DIR
            redirectURL = ID
            return render(request, 'upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'redirectURL': redirectURL
            })
        else:
            return render(request, 'upload.html') #reset upload page if not allowed
            #TODO add 'filetype not allowed' message to user
    return render(request, 'upload.html')

def results(request, ID):#, subpage):
    
    print(ID)
    exists =  DIRcheck(ID, MEDIA_ROOT)
    print(exists)
    if exists != -1:
        return render(request, "results.html")#, {"subpage": subpage})
    else:
        return render(request, 'upload.html')

def about(request):

    return render(request, 'about.html')


def contact(request):

	return render(request, 'contact.html')
