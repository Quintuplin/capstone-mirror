from django.urls import re_path
from django.urls import path

from . import views
#these are the urls within our upload app
urlpatterns = [
	path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
	path('home/', views.upload_file, name='home'),

]
