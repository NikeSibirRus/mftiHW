from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from users.models import Account
from .forms import  *
from .forms import UserRegisterForm

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
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан  {username}: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')