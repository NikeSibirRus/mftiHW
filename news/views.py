from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

from .models import *
from django.db import connection, reset_queries
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def all_news(request):
    article = Article.objects.all()
    context = {'article': article}

    return render(request, 'news/all_news.html', context)

def index(request):
   # article = Article.objects.last()
    article = Article.objects.latest("id")
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

def addnews(request):
    return render(request, 'news/addnews.html')


@login_required(login_url="/")
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None:
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save()
                form = ArticleForm()
                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request, 'news/add_article.html', {'form': form})
