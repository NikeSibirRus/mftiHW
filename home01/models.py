from django.db import models

# Create your models here.
class News:
    def __init__(self, category, author, date, heading, title, title2, content, addition):
        self.category = category #Категория новости
        self.author = author #автор
        self.date = date #дата
        self.heading = heading  # заголовок
        self.title = title  # название
        self.title2 = title2  # доп название
        self.content = content  # содержание
        self.addition = addition  # дополнение
    def __str__(self):
        return f'{self.heading}: {self.title}, {self.content}'