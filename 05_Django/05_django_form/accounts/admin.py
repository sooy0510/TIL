from django.contrib import admin
# 장고가 미리 admin class 만들어놓음
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)