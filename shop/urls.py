from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.apps import ShopConfig
from shop.views import (ProductCreateView,SubjectListView, SubjectUpdateView)

app_name = ShopConfig.name



urlpatterns = [
    # path('product/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('subject/', SubjectListView.as_view(), name='subject_list'),
    path('subject/update/<int:pk>/', SubjectListView.as_view(), name='subject_update'),


    # path('subject/<int:category>/', SubjectListView.as_view(), name='subject'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)