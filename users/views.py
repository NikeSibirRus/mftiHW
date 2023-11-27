from django.shortcuts import render, HttpResponse

from users.models import Account



# Create your views here.
def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc)
    return HttpResponse('Приложение Users')


