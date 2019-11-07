from django.contrib import admin
from .models import Article, Comment

# Register your models here.


class articleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)


class commentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'content', 'created_at', 'updated_at')


admin.site.register(Article, articleAdmin)
admin.site.register(Comment, commentAdmin)
