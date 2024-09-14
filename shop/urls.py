from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.apps import ShopConfig
from shop.views import (SubjectListView, SubjectUpdateView, CategoryDetailView, ProductUpdateView)

app_name = ShopConfig.name



urlpatterns = [
    # path('product/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('subject/', SubjectListView.as_view(), name='subject_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', SubjectUpdateView.as_view(), name='subject_update'),
####
    path('subject/<int:pk>/', SubjectListView.as_view(), name='subject'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)