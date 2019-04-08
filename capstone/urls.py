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

# urlpatterns += staticfiles_urlpatterns()

#https://stackoverflow.com/questions/6418072/accessing-media-files-in-django
from django.conf import settings
from django.conf.urls import url, include
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    ]