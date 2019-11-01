# 2019-11-01(금) Movie List 프로젝트

## 1. Pylint

### 1.1 Pylint

>  Python 코드의 오류를 검사하고 적절한 Python 코딩 패턴을 권장하며 널리 사용되는 도구

<br>

### 1.2 설치

```bash
$ pip install pylint
```

<br>

### 1.3 pylint에 django 기능 추가

```bash
$ pip install pylint-django
```

<br>

### 1.4 setting.py 수정

- `ctrl+shift+p` : Open Settings(json) 

```django
{
    "workbench.startupEditor": "newUntitledFile",
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "editor.tabSize": 2,
    "liveServer.settings.donotShowInfoMsg": true,
	<!-- 아래부터 추가 -->
    "python.linting.pylintArgs":[
        "--load-plugins=pylint_django",
        "--erros-only"
    ]
}
```

<br>

<br>

<br>



# MOVIE LIST 프로젝트

## 1. Django Project 생성 & 설정

## 2. Bootstrap 적용

### 2.1 다운받은 Bootstrap 프로젝트에 추가하기

- 참고 블로그

  >  https://pyrois.tistory.com/6 

<br>

#### 프로젝트 구조

- App에 static 폴더 만들고 다운받은 `assets`,` images `폴더 넣어주기

```django
connected_PJT1
	/config
	/movies
		/static
			/assets
				/css
				/fonts
				/js

			/images
```



> ![1572593417042](images/1572593417042.png)

<br>

<br>

#### `settings.py` 수정

- `settings.py` 맨 아래로 가서 `STATIC_ROOT` 추가
- `STATIC_ROOT` :   static 파일들을 찾는 경로를 나타내는 `STATIC_ROOT` 라는 변수를 설정 

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

<br>

<br>

### 2.2 Bootstrap 적용

#### `base.html`수정

- 나는 `base.html`을 다 상속받아서 쓸 것이기 때문에 `base.html`에 bootstrap에서 사용하는 CSS와 Script들을 모두 추가해주었다

  - 이미지 클릭하면 팝업뜨는 script파일은 제외함

  <br>

- `{% load staticfiles %}`

  - 템플릿 상단에 태그 반드시 명시!
  - staticfiles를 사용하겠다는 뜻

  <br>

- `{% static 'assets/css/main.css' %}`

  - **static templete tag**를 이용해서 해당  리소스 지정

  <br>

- `CSS`, `script`, `img` 태그의 `href`,`src` 속성 모두 수정해주기

  ```django
  {% load staticfiles %}
  
  <!DOCTYPE HTML>
  <!--
  	Visualize by TEMPLATED
  	templated.co @templatedco
  	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
  -->
  <html>
  	<head>
  		<title>MOVIE LIST</title>
  		<meta charset="utf-8" />
  		<meta name="viewport" content="width=device-width, initial-scale=1" />
  		<link rel="stylesheet" href="{% static 'assets/css/main.css' %}" />
  	</head>
  	<body>
      <!-- Wrapper -->
      <div id="wrapper">
            <!-- Header -->
          <header id="header">
            <span class="avatar"><a href="{% url 'movies:index' %}"><img src="{% static 'images/cat.jpg' %}" alt="" /></a></span>
            {% block header %}
            <h1>이곳은 <strong>영화</strong>를 소개해주는 곳입니다</h1>
            <h1 class='text-center'><a href="{% url 'movies:new' %}">영화 등록</a></h1>
            <ul class="icons">
              <li><a href="#" class="icon style2 fa-twitter"><span class="label">Twitter</span></a></li>
              <li><a href="#" class="icon style2 fa-facebook"><span class="label">Facebook</span></a></li>
              <li><a href="#" class="icon style2 fa-instagram"><span class="label">Instagram</span></a></li>
              <li><a href="#" class="icon style2 fa-500px"><span class="label">500px</span></a></li>
              <li><a href="#" class="icon style2 fa-envelope-o"><span class="label">Email</span></a></li>
            </ul>
            {% endblock  %}
          </header>
    {% block body %}
  
    {% endblock  %}
  
      <!-- Footer -->
        <footer id="footer">
          <p>&copy; Untitled. All rights reserved. Design: <a href="http://templated.co">TEMPLATED</a>. Demo Images: <a href="http://unsplash.com">Unsplash</a>.</p>
        </footer>
  
    </div>
  
  		<!-- Scripts -->
  			<script src="{% static 'assets/js/jquery.min.js' %}"></script>
  			{% comment %} <script src="{% static 'assets/js/jquery.poptrox.min.js' %}"></script> {% endcomment %}
  			<script src="{% static 'assets/js/skel.min.js' %}"></script>
  			<script src="{% static 'assets/js/main.js' %}"></script>
  
  	</body>
  </html>
  ```

   

<br>

<br>

#### base.html을 상속받은 템플릿

- `{% load staticfiles %}`

  - **extends templete tag**를 통해 base.html을 상속받은 템플릿의 상단에도 반드시 `{% load staticfiles %}`를 써주어야 한다
  - 순서는 `{% extends 'base.html' %}` =>  `{% load staticfiles %}` 
  - 순서바뀌면 에러남

  ```django
  {% extends 'base.html' %}
  {% load staticfiles %}
  
  {% block header %}
      <h1>이곳은 <strong>영화</strong>를 등록해주는 곳입니다</h1>
  {% endblock  %}
  
  {% block body %}
  ...
  {% endblock  %}
  ```

  

