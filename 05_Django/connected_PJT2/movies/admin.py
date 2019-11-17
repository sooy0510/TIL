from django.contrib import admin
from .models import Movie, Rating

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
  list_display = ('pk', 'title', 'created_at', 'updated_at')

class RatingAdmin(admin.ModelAdmin):
  list_display = ('pk', 'score', 'content', 'created_at', 'updated_at', 'user')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
    