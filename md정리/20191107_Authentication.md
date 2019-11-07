# 1. Authentication(인증)

> 장고에서 이미 Auth 관련 기능을 만들어두었고, 우리는 자연스럽게 사용하고 있었다. `createsuperuser`를 통해 관리자 계정도 만들었고, Admin 페이지에서 로그인 기능도 사용하고 있었다.

<br>

## 1.1 Accounts 앱 추가

- 기존 앱에서 구현해도 되지만, 장고에서는 기능 단위로 애플리케이션을 나누는 것이 일반적이므로 `accounts` 라는 새로운 앱을 만들어보자
- `accounts` 앱 생성 / 등록
- URL 분리

<br>

<br>

## 1.2 UserCreationForm

> django에서는 새로운 사용자를 위한 회원가입 form을 제공하고 있다

<br>

- `signup.html`

  ```python
  # views.py
  
  from django.contrib.auth.forms import UserCreationForm
  
  # Authentication(인증) -> 신원 확인
  # - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것
  
  # Create your views here.
  
  # Auth CRUD : CREATE
  def signup(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('articles:index')
    else:
      form = UserCreationForm()
  
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)
  ```

  

<br>

<br>

사용자가 session의 기능을 몰라도 django가 session의 기능을 모두 제공해줌

