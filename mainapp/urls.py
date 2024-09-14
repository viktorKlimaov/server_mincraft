from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mainapp.apps import MainappConfig
from mainapp.views import (MyMainListView, ProductCreateView, EmailCreateView, EmailUpdateView, EmailListView)

app_name = MainappConfig.name



urlpatterns = [
    path('', MyMainListView.as_view(), name='my_main'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    # path('product/delete/', ProductDeleteView.as_view(), name='delete_product'),
#####
    path('email/', EmailListView.as_view(), name='email'),
    path('email/create/', EmailCreateView.as_view(), name='email_create'),
    path('email/update/<int:pk>/', EmailUpdateView.as_view(), name='email_update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

