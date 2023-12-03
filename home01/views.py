from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    return render(request, 'home01/index.html')

def aboutus(request):
    return render(request, 'home01/aboutus.html')

def contacts(request):
    return render(request, 'home01/contacts.html')

def err404(request, exception):
    return render(request, 'home01/404.html')
