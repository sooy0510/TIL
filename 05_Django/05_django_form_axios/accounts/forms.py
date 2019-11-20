from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# UserChangeForm상속받아서 customizing
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    # User 클래스를 바로 가져와서 사용하는 것이 아니라 
    # get_user_model()을 사용해서 User 클래스를 참조
    model = get_user_model()
    # UserChangeForm => User 클래스 => AbstractUser 클래스 상속 순
    # 이정도만 사용자가 수정할 수 있도록 변경
    # Django 공식문서 : user-model
    fields = ('email', 'last_name', 'first_name',)


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ('username', 'password1', 'password2', 'email', )