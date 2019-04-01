from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .modules.IDGEN import DIRgen, allowed_file
from capstone.settings import MEDIA_ROOT

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        if allowed_file(myfile.name):
            DIR = DIRgen(MEDIA_ROOT)
            fs = FileSystemStorage(location=DIR)
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = DIR
            redirectURL = '/dash_results/'
            return render(request, 'upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'redirectURL': redirectURL
            })
        else:
            return render(request, 'upload.html') #reset upload page if not allowed
            #TODO add 'filetype not allowed' message to user
    return render(request, 'upload.html')


def about(request):

    return render(request, 'about.html')


def contact(request):

	return render(request, 'contact.html')
