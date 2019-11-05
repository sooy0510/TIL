from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
  articles = Article.objects.all()[::-1] #python
  context = {'articles':articles}
  return render(request,'articles/index.html', context)


# 사용자에게 게시글 작성 폼을 보여주는 함수
# def new(request):
#   return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
  # 실제 DB에 저장
  if request.method == 'POST':
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

    # .html 파일 내에서 '{% url %} 템플릿 태그' 사용햇을때(헷갈림 주의!)
    # <a href="{% url 'articles:detail' article.pk %}">[[DETAIL]]</a>
  # 사용자에 NEW Form 전달하기
  else:
    return render(request, 'articles/create.html')




# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  context = {'article':article}
  return render(request, 'articles/detail.html',context)


def delete(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  article.delete()
  return redirect('articles:index')


# 사용자한테 게시글 수정 폼을 전달
# def edit(request, article_pk):
#   article = Article.objects.get(pk=article_pk)
#   context = {'article':article}
#   return render(request, 'articles/edit.html', context)


# 수정 내용 전달받아서 DB에 저장(반영)
def update(request, article_pk):
  # 수정 내용 실제 DB에 반영
  if request.method == 'POST':
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    #return redirect(f'/articles/{article.pk}/')
    return redirect('articles:detail', article.pk)
  
  # 사용자한테 게시글 수정 폼을 전달
  else:
    article = Article.objects.get(pk=article_pk)
    context = {'article':article}
    return render(request, 'articles/update.html', context)

# 댓글 등록
def comments_create(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method == 'POST':
    content = request.POST.get('content')
    comment = Comment(article=article, content=content)
    comment.save()
  return redirect('articles:detail', article.pk)
