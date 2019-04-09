from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.urls import path

import threading, time

from .modules.APP1 import DIRgen, allowed_file
from .modules.APP3 import RESULTgen
from .modules.APP2 import DIRcheck, RESULTcheck
from capstone.settings import MEDIA_ROOT, STATIC_ROOT

def APP3_Thread(ID, MEDIA_ROOT, STATIC_ROOT):
    print (threading.currentThread().getName(), 'Starting')
    time.sleep(10) #this is to simulate APP3 calculation time
    RESULTgen(ID, MEDIA_ROOT, STATIC_ROOT)
    print (threading.currentThread().getName(), 'Exiting')

def APP2_Thread(request, uploaded_file_url, redirectURL):
    print (threading.currentThread().getName(), 'Starting')
    print (threading.currentThread().getName(), 'Exiting')

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        if allowed_file(myfile.name):
            ID, DIR = DIRgen(MEDIA_ROOT)
            fs = FileSystemStorage(location=DIR)
            fs.save(myfile.name, myfile)
            uploaded_file_url = DIR
            redirectURL = ID

            A3 = threading.Thread(name="APP3", target=APP3_Thread, args = (ID, MEDIA_ROOT, STATIC_ROOT))
            A2 = threading.Thread(name="APP2", target=APP2_Thread, args = (request, uploaded_file_url, redirectURL))
            
            A3.start()
            A2.start()
            
            return render(request, 'upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'redirectURL': redirectURL
            })
        else:
            return redirect('home')
    return render(request, 'upload.html')

# def results(request, ID):#, subpage):
#     print("ID: " + ID)
#     DIRexists =  DIRcheck(ID, MEDIA_ROOT)
#     print("DIR: " + str(DIRexists))
#     if DIRexists != -1:
#         if RESULTcheck(ID, MEDIA_ROOT) == True:
#             return render(request, "results.html")
#         else: return render(request, "wait.html")
#     else:
#         return redirect('home')

def results(request, ID, subpage=None):
    print("ID: " + ID)
    DIRexists =  DIRcheck(ID, MEDIA_ROOT)
    print("DIR: " + str(DIRexists))
    if DIRexists != -1:
        if RESULTcheck(ID, MEDIA_ROOT) == True:
            if subpage is not None:
                return render(request, "res1.html")
            else: return render(request, "results.html")
        else: return render(request, "wait.html")
    else:
        return redirect('home')

def about(request):

    return render(request, 'about.html')


def contact(request):

	return render(request, 'contact.html')
