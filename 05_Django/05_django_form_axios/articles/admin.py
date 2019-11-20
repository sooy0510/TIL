from django.contrib import admin
from .models import Article, Comment, Hashtag

# Register your models here.


class articleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)


class commentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'content', 'created_at', 'updated_at')

class hashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Comment, commentAdmin)
admin.site.register(Article, articleAdmin)
admin.site.register(Hashtag, hashtagAdmin)
