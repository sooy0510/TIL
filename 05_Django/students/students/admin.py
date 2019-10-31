from django.contrib import admin
from .models import Student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
  list_display = ('pk','name','birthday','created_at','updated_at')


admin.site.register(Student, studentAdmin)