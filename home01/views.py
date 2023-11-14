from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    n1 = News('Здоровье'
              ,'Journalist001'
              ,'10.11.2023'
              ,'Горячие новости!!!'
              ,'Роспотребнадзор: нас ожидает вторая волна заболеваемости COVID-19 <a href="https://news.mail.ru/society/58533827/?frommail=1">Первоисточник</a>'
              ,'Эксперты расценили ситуацию повышения заболеваемости как начало эпидемии.'
              ,''
              ,'Ранее Роспотребнадзор просил новосибирцев не стесняться носить медицинские маски.'
              )
    l = [n1]
    context = {'numbers': l
    }

    return render(request, 'home01/index.html', context)

def aboutus(request):
    return render(request, 'home01/aboutus.html')

def all_news(request):
    return render(request, 'home01/all_news.html')

def contacts(request):
    return render(request, 'home01/contacts.html')

def addnews(request):
    return render(request, 'home01/addnews.html')

def login(request):
    if request.method == 'POST':
        print('Получили post-Запрос!')
        print(request.POST)
        print(request.POST.get('username'))
        print(request.POST.get('password'))
    else:
        print('Получили get-Запрос!')





    return render(request, 'home01/login.html')

def cr_account(request):
    return render(request, 'home01/cr_account.html')

def err404(request, exception):
    return render(request, 'home01/404.html')
