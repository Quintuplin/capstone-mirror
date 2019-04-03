"""capstone URL Configuration
edit the webapp.urls instead
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", include("webapp.urls")),
    path("admin/", admin.site.urls),  # Activates the admin interface
]

urlpatterns += staticfiles_urlpatterns()
