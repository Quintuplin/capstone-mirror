from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf.urls import url
from . import views

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)

"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
	path('about/', views.about, name='about'),
    path('about', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),
	path('home/', views.upload, name='home'),
    path('home', views.upload, name='home'),
    path('upload/', views.upload, name='home'),
    path('upload', views.upload, name='home'),
    path('', views.upload, name='home'),
#     re_path(r'^[\w]', views.results, name="results"), ##everything else gets routed through views.results
    path('<ID>', views.results, name='results'),
]
