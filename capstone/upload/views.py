from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

#this method was retrieved from stack overflow on 3.14.19
def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        redirectURL = '/dash_results/'
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'redirectURL': redirectURL
        })
    return render(request, 'upload.html')