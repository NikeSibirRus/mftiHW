from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

from .models import *
from django.db import connection, reset_queries
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def all_news(request):
    categories = Article.categories  # создали перечень категорий
    author_list = User.objects.all()  # создали перечень авторов

    if request.method == "POST":
        selected_author = int(request.POST.get('author_filter'))
        selected_category = int(request.POST.get('category_filter'))
        if selected_author == 0:  # выбраны все авторы
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected_author)
        if selected_category != 0:  # фильтруем найденные по авторам результаты по категориям
            articles = articles.filter(category__icontains=categories[selected_category - 1][0])
    else:  # если страница открывется впервые
        selected_author = 0
        selected_category = 0
        articles = Article.objects.all()

    context = {'articles': articles, 'author_list': author_list, 'selected_author': selected_author,
               'categories': categories, 'selected_category': selected_category}

    return render(request, 'news/all_news.html', context)

def index(request):
   # article = Article.objects.last()
    article = Article.objects.latest("id")
    context = {'article':article}
    return render(request,'news/index.html',context)


def news_detail(request, id):
    article = Article.objects.filter(id=id).first()
    context = {'article': article}
    return render(request,'news/index.html',context)



@login_required(login_url="/")
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None:
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save()
                form.save_m2m()  # сохраняем теги
                for img in request.FILES.getlist('image_field'):
                    Image.objects.create(article=new_article, image=img, name=img.name)
                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request, 'news/add_article.html', {'form': form})
