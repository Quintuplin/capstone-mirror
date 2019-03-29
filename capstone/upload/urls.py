from django.urls import re_path

from . import views

urlpatterns = [
	path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
