from django.shortcuts import render


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}\n{email}')

    return render(request, 'main/index.html')
