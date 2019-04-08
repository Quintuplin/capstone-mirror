"""capstone URL Configuration
edit the webapp.urls instead
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path("", include("webapp.urls")),
    path("admin/", admin.site.urls),  # Activates the admin interface
]

# urlpatterns += staticfiles_urlpatterns()

#https://stackoverflow.com/questions/6418072/accessing-media-files-in-django
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        re_path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    ]