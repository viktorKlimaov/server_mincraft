from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.views import index, my_main

urlpatterns = [
    path('my/', index),
    path('', my_main)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

