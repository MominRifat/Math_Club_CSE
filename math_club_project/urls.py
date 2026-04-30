from os import stat

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from math_club_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('gallery/', include('gallery_app.urls')),
    path('events/', include('events_app.urls')),
    path('team/', include('team_app.urls')),
    path('quiz/', include('quiz_app.urls')),
    path('join/', include('join_app.urls')),
    path('contact/', include('contact_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)