from IPython import embed
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Authentication(인증) -> 신원 확인
# - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

# Create your views here.

# Auth CRUD : CREATE
def signup(request):
  if request.user.is_authenticated:
    return redirect('articles:index')
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    #embed()
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('articles:index')
  else:
    form = CustomUserCreationForm()

  context = {'form':form}
  return render(request, 'accounts/auth_form.html', context) 


def login(request):
  #embed()
  # 이미 login되어있는 사용자가 다시 로그인 시도할때
  if request.user.is_authenticated:
    return redirect('articles:index')
 
  if request.method == 'POST':
    # login은 session 정보가 있기때문에 request 넘겨줘야함
    form = AuthenticationForm(request, request.POST)
    #embed()
    if form.is_valid():
      # AuthenticationForm이 들고잇는 사용자 정보를 들고온다
      auth_login(request, form.get_user())
      #return redirect('articles:index')
      return redirect(request.GET.get('next') or 'articles:index')
  else:
    form = AuthenticationForm()
  
  context = { 'form':form }
  return render(request, 'accounts/auth_form.html', context)


def logout(request):
  # 이서버에서 보고 있는 session에서 login 정보를 지워버림
  auth_logout(request)
  return redirect('articles:index')

@require_POST
def delete(request):
  # 지금 접속하고 있는 user 바로 삭제
  request.user.delete()
  return redirect('articles:index')

# 회원정보 수정
@login_required
def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {'form':form}
  return render(request, 'accounts/auth_form.html', context)

@login_required
def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request,user)
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {'form':form}
  return render(request, 'accounts/auth_form.html', context)
