from django.shortcuts import render, HttpResponse

from users.models import Account
from .forms import  *

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


