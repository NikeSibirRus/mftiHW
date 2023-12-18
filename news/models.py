from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from django.db.models import Count


# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=80)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    def tag_count(self):
        count = self.article_set.count()
        #комментарий: когда мы работаем со связанными объектами (foreign_key, m2m, один к одному),
        #мы можем обращаться к связанным таблицам при помощи синтаксиса:
        #связаннаяМодель_set и что-то делать с результатами. В этом примере - мы используем связанные article
        #и вызываем метод count
        return count
    class Meta:
        ordering = ['title','status']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(models.Model):
    categories = (('E','Economics'),
                  ('S','Science'),
                  ('IT','IT'))

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    title = models.CharField('Заголовок', max_length=50, default='')
    anouncement = models.TextField('Аннотация', max_length=250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата создания', auto_now=True)
    category = models.CharField(choices=categories, max_length=50, default='', verbose_name='Категория')
    tags = models.ManyToManyField(to=Tag, blank=True, verbose_name='Тэги')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title} от: {str(self.date)[:10]}'

    def get_absolute_url(self):
        return f'/news/show/{self.id}'

    def tag_list(self):
        s = ''
        for t in self.tags.all():
            s = t.title
        return s

    def image_tag(self):
        image = Image.objects.filter(article=self)
        print('!!!!',image)
        if image:
            return mark_safe(f'<img src="{image[0].image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'

    #Методанные
    class Meta:
        ordering = ['title', 'date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='article_images/')
    def __str__(self):
        return self.name
    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'


class ViewCount(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,
                                related_name='views')
    ip_address = models.GenericIPAddressField()
    view_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-view_date',)
        indexes = [models.Index(fields=['-view_date'])]

    def __str__(self):
        return self.article.title