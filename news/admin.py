from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-date','title','author']
    list_display = ['title', 'author', 'date']
    list_filter = ['title', 'author', 'date']

    prepopulated_fields = {"slug": ("title", "author")}
    list_per_page = 6


admin.site.register(Article, ArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','tag_count']
    list_filter = ['title', 'status']

    @admin.display(description='Использований:', ordering='tag_count')
    def tag_count(self, object):
        return object.tag_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(tag_count=Count('article'))
        return queryset


admin.site.register(Tag, TagAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name','article','image_tag']