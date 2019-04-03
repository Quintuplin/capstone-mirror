from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from .modules.IDGEN import DIRgen, allowed_file
from capstone.settings import MEDIA_ROOT

#this method was retrieved from stack overflow on 3.14.19
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        if allowed_file(myfile.name):
            DIR = DIRgen(MEDIA_ROOT)
            fs = FileSystemStorage(location=DIR)
            fs.save(myfile.name, myfile)
            uploaded_file_url = DIR
            redirectURL = '/results/'
            return render(request, 'upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'redirectURL': redirectURL
            })
        else:
            return render(request, 'upload.html') #reset upload page if not allowed
            #TODO add 'filetype not allowed' message to user
    return render(request, 'upload.html')

def results(request):#, subpage):
    """Renders the results page.
    Args: subpage for subpage results
    """
    return render(request, "results.html")#, {"subpage": subpage})

def about(request):

    return render(request, 'about.html')


def contact(request):

	return render(request, 'contact.html')
