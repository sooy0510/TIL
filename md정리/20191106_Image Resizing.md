# 2019-11-06 (수)

## 1. Image Resizing

### 1.1 Python & Django 이미지 관련 라이브러리

```bash
# 설치 순서 주의! (의존성 있음)

$ pip install Pillow
$ pip install pilkit
$ pip install django-imagekit
```

<br>

- `pillow` : PIL(Python Image Library) 프로젝트에서 fork 되어서 나온 라이브러리. Python3를 지원하지 않기 때문에 Pillow를 많이 씀

- `pilkit` : Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리. 다양한 Processors 지원
  - Thumbnail
  - Resize
  - Crop...
- `django-imagekit` : 이미지 썸네일 Helper

<br>

<br>

### 1.2 INSTALLED_APPS 등록

```python
# settings.py

INSTALLED_APPS = [
	...
    'imagekit',
	...
]
```

<br>

<br>

### 1.3 모델 수정

- 현재는 `Django`에서 제공하는 `ImageField` 사용 중

- `imagekit` 에서 제공하는 `field` 쓰도록 모델 수정

  ```python
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
    ...
    image = ProcessedImageField(
      processors=[Thumbnail(200,300)],  	# 처리할 작업
      format='JPEG',                    	# 이미지 포맷
      options={'quality':90},           	# 각종 추가 옵션
      upload_to='articles/images',      	# 저장 위치   
      # 실제경로 -> MEDIA_ROOT/articles/images
    )
    ... 
  ```

<br>

<br>

### 1.4 Migrations

- `ProcessdImageField`의 인자로 들어가는 옵션들은 수정을 하더라도 다시 `migration ` 하지 않아도 바로바로 적용이 된다.

<br>

<br>

<br>



## 2. Favicon

### 2.1  **favicon.ico** 만들기

> Favicon Generator :  https://www.favicon-generator.org/ 

<br>

<br>

### 2.2 static 경로에 추가

- `static` 경로에 `favicon`폴더 추가

  > ![1573003599980](images/1573003599980.png)

<br>

<br>

### 2.3 Template 적용

- 템플릿 상단에 `{% load static %}` 반드시 추가

  ```django
  {% load static %}
  ...
  <head>
    ...
    <title>Django CRUD</title>
    <link rel="shortcut icon" href="{% static 'articles/favicon/favicon.ico' %}" type="image/x-icon">
    <link rel="icon" href="{% static 'articles/favicon/favicon.ico' %}" type="image/x-icon">
    ...
  </head>
  ```

  

<br>

<br>

<br>