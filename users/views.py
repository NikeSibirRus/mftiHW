from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .models import *
from .forms import *

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data)
        else:
            print(form.errors)

    else:
        form = ContactForm()

    context={'form': form}
    return render(request,'users/contact_page.html',context)




from django.contrib.auth.decorators import login_required
from news.models import Article
@login_required
def add_to_favorites(request, id):
    article = Article.objects.get(id=id)
    #проверям есть ли такая закладка с этой новостью
    bookmark = FavoriteArticle.objects.filter(user=request.user.id,
                                              article=article)
    if bookmark.exists():
        bookmark.delete()
        messages.warning(request,f"Новость {article.title} удалена из закладок")
    else:
        bookmark = FavoriteArticle.objects.create(user=request.user, article=article)
        messages.success(request,f"Новость {article.title} добавлена в закладки")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc)
    return HttpResponse('Приложение Users')


def login(request):
    if request.method == 'POST':
        print('Получили post-Запрос!')
        print(request.POST)
        print(request.POST.get('username'))
        print(request.POST.get('password'))
    else:
        print('Получили get-Запрос!')
    return render(request, 'users/login.html')

def cr_account(request):
    return render(request, 'users/cr_account.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Добавляем группу
            category = request.POST['account_type']
            if category == 'Autors':
                group = Group.objects.get(name='Actions Required')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='Reader')
                user.groups.add(group)
            username = form.cleaned_data.get('username')
            Account.objects.create(user=user, nickname=user.username)

            messages.success(request, f'Ваш аккаунт создан  {username}: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    return render(request, 'users/profile.html')


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
def password_update(request):
    user = request.user
    form = PasswordChangeForm(user,request.POST)
    if request.method == 'POST':
        if form.is_valid():
            password_info = form.save()
            update_session_auth_hash(request,password_info)
            messages.success(request,'Пароль успешно изменен')
            return redirect('profile')

    context = {"form": form}
    return render(request,'users/edit_password.html',context)


def profile_update(request):
    user = request.user
    account = Account.objects.get(user=user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            messages.success(request,"Профиль успешно обновлен")
            return redirect('profile')
        else:
            pass
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user)}
    return render(request,'users/edit_profile.html',context)