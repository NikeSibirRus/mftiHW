from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def all_news(request):
    article = Article.objects.all()
    context = {'article': article}

    return render(request, 'news/all_news.html', context)

def index(request):
    article = Article.objects.all().last()
    context = {'article':article}
    return render(request,'news/index.html',context)


def news_detail(request, id):
    article = Article.objects.filter(id=id).first()
    print('News: '+str(id))
    print(article.title)
    return HttpResponse(f'<h1>{article.title}</h1>')

def news_add(request):
    avthor = User.objects.get(id=request.user.id)
    print(avthor)
    article = Article(author=avthor,
                      title='Заголовок новости',
                      anouncement='Описание новости',
                      text='Содержание'
                      )
    article.save()
    return HttpResponse(f'<h1>{article.title}</h1>')

