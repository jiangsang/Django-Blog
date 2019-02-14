from django.contrib import admin
from .models import Article,Photo
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'update_time')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Photo, PhotoAdmin)