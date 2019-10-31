# 19.10.30(수) Django CRUD 구현

## 0. 사전작업

### 0.1 프로젝트 생성

```bash
$ cd 03_django_crud
```



```bash
$ django-admin startproject config .
```

<br>

<br>

### 0.2 애플리케이션 생성

```bash
$ python manage.py startapp articles
```

```python
# settings.py : 출생신고 까먹지말자........
INSTALLED_APPS = [
    'articles',
    ...
]
```

<br>

<br>



### 0.3 URL 분리(위임)

```python
# config/urls.py

from django.urls import path, include

urlpatterns = [
    # 요청 경로가 articles/로 시작하면 articles 앱 안에 있는 urls.py로 이동!
    path('articles/', include('articles.urls')),
    ...
]
```



```python
# articles/urls.py

from . import views

urlpatterns = [
    # articles/ 로 요청했을 경우 index 함수 실행
    path('', views.index),
]
```

<br>

<br>

### 0.4 템플릿 경로 커스터마이징 + base.html

> https://getbootstrap.com/docs/4.3/getting-started/introduction/

```html
<!-- base.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Django CRUD</title>

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>
  <div class="container">
    {% block body %}
    {% endblock  %}
  </div>

  <!-- Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>
```



<br>

<br>

### 0.5 데이터베이스 모델링

```python
# models.py

from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=40)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 객체 표시 형식 수정
  def __str__(self):
    return f'[{self.pk}] {self.title}'
```

<br>

#### `makemigrations `: 설계도 만들기

```bash
$ python manage.py makemigrations
```

```
03_django_crud/
	config/
	articles/
		migrations/
			0001_initial.py
```

<br>

#### `migrate` : 실제 DB에 반영하기

```bash
$ python manage.py migrate
```

<br>

- 추가 정보

  - `showmigrations`: makemigrations를 통해 만든 설계도가 실제 DB에 반영된 상태인지 아닌지 확인

  - `sqlmigrate`: 실제 DB에 반영하기 전 SQL 쿼리문으로 바뀐 모습 확인

    ```bash
    $ python manage.py sqlmigrate articles 0001
    ```

    



<br>

<br>



### 0.6 django- extensions



1. 설치

   ```bash
   $ pip install django-extensions
   ```

2. 앱 등록

   - third party app이기 때문에 `settings.py`에 등록

   ```python
   INSTALLED_APPS = [
       # Local apps
       'articles',
       
       #Third party apps
       'django_extensions',
       
       # Django apps(장고 기본 앱들)
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

3. Shell 실행

   ```bash
   $ python manage.py shell_plus
   ```

   

<br>

## 1. CREATE

### 1.1 기본적으로 두 개의 뷰 함수로 구성된다

- GET은 쿼리스트링에 데이터가 노출되니 POST로 구현!
- {% csrf token %}꼭 써주기

1. 사용자에게 HTML Form을 던져줄 함수
2. HTML Form에서 데이터를 전달받아서 실제 DB에 저장하는 함수

```python
# articles/views.py

# 사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
  return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
  title = request.POST.get('title')
  content = request.POST.get('content')

  article = Article(title=title, content=content)
  article.save()
  # render는 html파일만 가져와서 띄워주는 함수
  # 경로는 create에 머물러 있다
  return render(request, 'articles/create.html')
  #return redirect('/articles/')
```

<br>

```html
<!-- base.html -->

{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">NEW</h1>
<form class="text-center" action="/articles/create/" method="POST">
  {% csrf_token %}
  TITLE: <input type="text" name="title"><br>
  CONTENT: <textarea name="content" cols="30" rows="10"></textarea><br>
  <input type="submit" value="등록">
</form>
<hr>
<!-- 뒤로가기 버튼 -->
<a href="/articles/">[BACK]</a>
{% endblock  %}
```

<br>

```html
<!-- config/templates/articles/create.html -->
{% extends 'base.html' %}

{% block body %}
<h2>글 작성이 완료됐습니다!</h2>
{% endblock  %}
```

<br>

<br>

### 1.2 등록확인

#### Admin 계정 만들어서 확인

```bash
$ python manage.py createsuperuser
```

```python
# admin.py

from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('pk','title','content','created_at','updated_at',)


admin.site.register(Article, ArticleAdmin)
```



<br>

<br>

### 1.3 Redirect

- 현재는 `등록`버튼을 누르면 `create.html`로 이동하는 상태

  1. 등록하면 `index.html`로 이동하도록 바꾸자

  ```python
  # articles/views.py
  
  from django.shortcuts import render, redirect
  
  # render는 html파일만 가져와서 띄워주는 함수
  # 경로는 create에 머물러 있다
  #return render(request, 'articles/create.html')
  return redirect('/articles/')
  ```

  <br>

  2. 등록하면 등록한 데이터의 상세페이지(`/detail`)로 이동하도록 수정
     - 객체를 `save`하면 `pk`값이 자동으로 부여됨

  ```python
  # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
  def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
  
    article = Article(title=title, content=content)
    # save까지하고 나면 pk값 부여됨
    article.save()
    
    return redirect(f'/articles/{article.pk}')
  ```

  



<br>

<br><br>

## 2. READ

### 2.1 index.html 상세정보 (index 로직)

```html
<!-- index.html -->

{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">Articles
<a href="/articles/new/">[NEW]</a>
</h1>
<hr>
{% for article in articles %}
<p>
  [{{ article.pk }}]{{ article.title }}
</p>
<a href="/articles/{{ article.pk }}">[DETAIL]</a>
<hr>
{% endfor %}

{% endblock  %}
```

<br>

```python
# articles/urls.py

urlpatterns = [
  ...
  # pk번호로 접근
  path('<int:article_pk>/', views.detail), 
]
```

<br>

```python
# articles/views.py : variable Routing 이용

# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  context = {'article':article}
  return render(request, 'articles/detail.html',context)
```

<br>

```html
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">DETAIL</h1>
<p>글 번호 : {{ article.pk }}</p>
<p>글 제목 : {{ article.title }}</p>
<p>글 내용 : {{ article.content }}</p>
<p>생성 시각 : {{ article.created_at }}</p>
<p>수정 시각 : {{ article.updated_at }}</p>
<hr>
<a href="/articles/">[BACK]</a>
{% endblock %}
```

<br>

<br>

<br>



## 3. DELETE

### 3.1 pk로 게시물 지우기

- 삭제 후에는 `index`페이지로 돌아감

```python
# articles/views.py

def delete(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  article.delete()
  return redirect('/articles/')
```

<br>

```html
<!-- /articles/detail.html -->

{% extends 'base.html' %}

{% block body %}
<h1 class="text-center">DETAIL</h1>
<p>글 번호 : {{ article.pk }}</p>
<p>글 제목 : {{ article.title }}</p>
<p>글 내용 : {{ article.content }}</p>
<p>생성 시각 : {{ article.created_at }}</p>
<p>수정 시각 : {{ article.updated_at }}</p>
<hr>
<a href="/articles/">[BACK]</a>
<a href="/articles/{{ article.pk }}/delete/">[DELETE]</a>
{% endblock %}
```

<br>

```python
# articles/urls.py

path('<int:article_pk>/delete/', views.delete), # DELETE Logic
```

<br>

<br>

## 4. UPDATE

### 4.1 수정 Form

- `detail.html`에서 `[EDIT]`버튼 누르면 수정폼(`edit.html`)을 전달

  ```python
  # articles/views.py
  
  # 사용자한테 게시글 수정 폼을 전달
  def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request, 'articles/edit.html', context)
  ```

  <br>

  ```html
  <!-- edit.html -->
  
  {% extends 'base.html' %}
  
  {% block body %}
  <h1 class="text-center">EDIT</h1>
  <form class="text-center" action="/articles/{{ article.pk }}/update/" method="POST">
    {% csrf_token %}
    TITLE: <input type="text" name="title" value={{ article.title }}><br>
    CONTENT: <textarea name="content" cols="30" rows="10">{{ article.content }}</textarea><br>
    <input type="submit" value="수정">
  </form>
  <hr>
  <!-- 뒤로가기 버튼 -->
  <a href="/articles/{{ article.pk }}/">[BACK]</a>
  {% endblock  %}
  ```

  <br>

  ```python
  # articles/urls.py
  
  ...
  path('<int:article_pk>/edit/', views.edit), # UPDATE Logic - 폼 전달
  ...
  ```

<br>

<br>

### 4.2 DB에 수정정보 저장

- DB에 UPDATE 후 상세페이지로 **REDIRECT** 

  ```python
  # articles/views.py
  
  # 수정 내용 전달받아서 DB에 저장(반영)
  def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')
  ```

  <br>

  ```python
  # articles/urls.py
  
  path('<int:article_pk>/update/', views.update), # UPDATE Logic - DB저장
  ```

  

<br>

<br>

## 5. URL patterns 수정

### 5.1 기존 URL patterns

- 각 애플리케이션의 view함수마다 접근 url 을 일일이 지정해주어야함

  ```python
  # 기존 articles/urls.py
  
  urlpatterns = [
    # 일반적으로 view함수와 똑같이 name바꿈
    path('', views.index, name='index'),  # READ Logic - Index
    path('new/', views.new, name='new'),  # CREATE Logic - 사용자에게 폼 전달
    path('create/', views.create, name='create'),  # CREATE Logic - 데이터베이스에 저장
    path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic
    # articles/9/delete 
    path('<int:article_pk>/edit/', views.edit, name='edit'), # UPDATE Logic-폼 전달
    path('<int:article_pk>/update/', views.update, name='update'), # UPDATE Logic-DB저장
  ]
  ```

  <br>

  ```html
  <!-- /aritcles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block body %}
  <h1 class="text-center">Articles
      
  <!-- url templete code 이용 : url 경로의 관리가 쉽다 -->
  <a href="{% url 'articles:new' %}">[NEW]</a>
  </h1>
  <hr>
  {% for article in articles %}
  <p>
    [{{ article.pk }}]{{ article.title }}
  </p>
  {% comment %} <a href="/articles/{{ article.pk }}">[DETAIL]</a> {% endcomment %}
  <a href="{% url 'articles:detail' article.pk %}">[[DETAIL]]</a>
  <hr>
  {% endfor %}
  
  {% endblock  %}
  ```

  

<br>

<br>



### 5.2 수정 URL patterns

#### URL 코딩방식

>#### .py  
>
>- 인자 넘길 때 `,`로 구분
>
>return redirect(f'/articles/{article.pk}/')    # 1. 하드코딩
>
>return redirect('articles:detail', article.pk)  # 2. URL namespace



> #### .html
>
> .html 파일 내에서 '{% url %} 템플릿 태그' 사용햇을때(헷갈림 주의!)
>
>- 인자 넘길 때 `,` 사용 X
>
>```html
> <a href="{% url 'articles:detail' article.pk %}">[[DETAIL]]</a>
>```

<br>

- url에 `name`을 지정해줘서 좀 더 편리하게 접근가능

- 일반적으로 view함수와 똑같이 `name`을 바꾼다!

- `app_name `추가해주면 똑같은 `name`으로 지정한 view함수를 사용하는 각각의 애플리케이션의 view함수에 접근이 가능하다

  - `{% url '앱이름:url name' %}`

  - ex`{% url 'articles:new' %}`

- html에서는 장고에 내장되어있는 `url templete tag` 이용

  - 인자 없을 때 : `{% url 'articles:new' %}`

  - 넘겨줄 인자 있을 때(순서대로) : `{% url 'articles:detail' article.pk %}`

  ```python
  # 수정 articles/urls.py
  
  app_name = 'articles'
  urlpatterns = [
    # 일반적으로 view함수와 똑같이 name바꿈
    path('', views.index, name='index'),  # READ Logic - Index
    path('new/', views.new, name='new'),  # CREATE Logic - 사용자에게 폼 전달
    path('create/', views.create, name='create'),  # CREATE Logic - 데이터베이스에 저장
    path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic
    # articles/9/delete 
    path('<int:article_pk>/edit/', views.edit, name='edit'), # UPDATE Logic - 폼 전달
    path('<int:article_pk>/update/', views.update, name='update'), # UPDATE Logic-DB저장
  ]
  ```

  <br>

  ```html
  <!-- /aritcles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block body %}
  <h1 class="text-center">Articles
  <!-- url templete code 이용 : url 경로의 관리가 쉽다 -->
  <a href="{% url 'articles:new' %}">[NEW]</a>
  </h1>
  <hr>
  {% for article in articles %}
  <p>
    [{{ article.pk }}]{{ article.title }}
  </p>
  <a href="{% url 'articles:detail' article.pk %}">[[DETAIL]]</a>
  <hr>
  {% endfor %}
  
{% endblock  %}
  ```
  
  <br>
  
  ```python
  # articles/views.py
  
  # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
  def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
  
    article = Article(title=title, content=content)
    # save까지하고 나면 pk값 부여됨
    article.save()
    
    # render는 html파일만 가져와서 띄워주는 함수
    # 경로는 create에 머물러 있다
    #return render(request, 'articles/create.html')
    #return redirect(f'/articles/{article.pk}/')    # 1. 하드코딩
    return redirect('articles:detail', article.pk)  # 2. URL namespace
  ```
  
  

<br>

<br>

<br>



# github 이미지 업로드

- 상대경로로 설정(`./images`)

![1572416700647](images/1572416700647.png)







