from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    gender_choices= (('M','Male'),('F','Female'),('N/A','Not answered'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Логин')
    nickname = models.CharField(max_length=100,verbose_name='Имя пользователя')
    birthdate = models.DateField(null=True, verbose_name='Дат рождения')
    gender = models.CharField(choices=gender_choices,max_length=20, default='N/A', verbose_name='Пол')
    account_image = models.ImageField(default='default.jpg', upload_to='account_images')

    address = models.CharField(max_length=100, null=True)
    vk = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    telegram = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.user.username} 's account "

    class Meta:
        ordering = ['user', 'nickname','gender']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'








