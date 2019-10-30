from django.contrib import admin
from .models import Article

# Register your models here
# admin.ModelAdmin을 상속받아 admin의 기능을 가져온다
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('pk','title','content',
  'created_at','updated_at',)
  list_display_links = ('content',)
  list_filter = ('created_at',)
  list_editable = ('title',)
  list_per_page = 2

# ArticleAdmin은 커스터마이징한 admin 클래스
admin.site.register(Article, ArticleAdmin) 