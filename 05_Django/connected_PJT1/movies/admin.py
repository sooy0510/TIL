from django.contrib import admin
from .models import Movie, Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
  list_display = ('pk','title','score',)

class CommentAdmin(admin.ModelAdmin):
  list_display = ('pk','content','created_at','updated_at',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)