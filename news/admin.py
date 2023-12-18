from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
from .models import *


class ArticleImageInline(admin.TabularInline):
    model = Image
    extra = 2
    readonly_fields = ('id','image_tag')

class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-date','title','author']
    list_display = ['title', 'author', 'date','symbols_count','image_tag']
    list_filter = ['title', 'author', 'date']
    list_display_links = ('date',)

    search_fields = ['title','tags__title']
    filter_horizontal = ['tags']

    prepopulated_fields = {"slug": ("title", "author")}
    list_per_page = 6
    inlines = [ArticleImageInline,]

    @admin.display(description='Длина', ordering='_symbols')
    def symbols_count(self, article: Article):
        return f"Символы: {len(article.text)}"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_symbols=Length('text'))
        return queryset


admin.site.register(Article, ArticleAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','tag_count']
    list_filter = ['title', 'status']
    actions = ['set_true']

    # @admin.display(description='Использований:', ordering='tag_count')
    # def tag_count(self, object):
    #     return object.tag_count
    #
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.annotate(tag_count=Count('article'))
    #     return queryset

    @admin.action(description='Активировать выбранные теги')
    def set_true(self,request,queryset):
        amount = queryset.update(status=True)
        self.message_user(request,f'Активировано {amount} тегов')


#admin.site.register(Tag, TagAdmin)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name','article','image_tag']

@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    list_display = ['article','ip_address','view_date']


