from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mainapp.apps import MainappConfig
from mainapp.views import (index, MyMainListView, ProductCreateView)

app_name = MainappConfig.name



urlpatterns = [
    path('forum', index, name='index'),
    path('', MyMainListView.as_view(), name='my_main'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    # path('product/delete/', ProductDeleteView.as_view(), name='delete_product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

