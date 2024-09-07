from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from mainapp.models import Product, Category


# Контроллер страницы для проверки
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}\n{email}')

    return render(request, 'mainapp/index.html')


# def my_main(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'mainapp/my_main.html', context)

class MyMainListView(ListView):
    """
    Контроллер отображения основой страницы
    """
    model = Product
    template_name = 'mainapp/my_main.html'

class ProductCreateView(CreateView):
    """
    Контроллер для создания товара
    """
    model = Product
    fields = ('name', 'description', 'image', 'category_id',
              'price', 'created_at', 'updated_at')

    success_url = reverse_lazy('mainapp:my_main')










