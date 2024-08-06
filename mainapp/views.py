from django.shortcuts import render


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}\n{email}')

    return render(request, 'mainapp/index.html')


def my_main(request):
    return render(request, 'mainapp/my_main.html')
