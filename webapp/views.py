from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .server import server

from datetime import datetime

from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import LogMessageForm
from .models import LogMessage

from .modules.IDGEN import DIRgen, allowed_file
from capstone.settings import MEDIA_ROOT

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

#this method was retrieved from stack overflow on 3.14.19
def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        if allowed_file(myfile.name):
            DIR = DIRgen(MEDIA_ROOT)
            fs = FileSystemStorage(location=DIR)
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = DIR
            redirectURL = '/results/'
            return render(request, 'webapp/upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'redirectURL': redirectURL
            })
        else:
            return render(request, 'webapp/upload.html') #reset upload page if not allowed
            #TODO add 'filetype not allowed' message to user
    return render(request, 'webapp/upload.html')

def disp_results(request):#, subpage):
    """Renders the results page.
    Args: subpage for subpage results
    """
    return render(request, "webapp/results.html")#, {"subpage": subpage})

class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    """Renders the about page."""
    return render(request, "webapp/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "webapp/contact.html")


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "webapp/hello_there.html", {"name": name, "date": datetime.now()}
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        else:
            return render(request, "webapp/log_message.html", {"form": form})
    else:
        return render(request, "webapp/log_message.html", {"form": form})

def dispatcher(request):
    '''
    Main function
    @param request: Request object
    '''

    params = {
        'data': request.body,
        'method': request.method,
        'content_type': request.content_type
    }
    with server.test_request_context(request.path, **params):
        server.preprocess_request()
        try:
            response = server.full_dispatch_request()
        except Exception as e:
            response = server.make_response(server.handle_exception(e))
        return response.get_data()


def dash_index(request, **kwargs):
    ''' '''
    return HttpResponse(dispatcher(request))


@csrf_exempt
def dash_ajax(request):
    ''' '''
    return HttpResponse(dispatcher(request), content_type='application/json')
