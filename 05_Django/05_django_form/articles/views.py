# http관련한 decorators import하기
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
 
# Create your views here.
def index(request):
  articles = Article.objects.all()
  context = {
    'articles':articles,
  }
  return render(request, 'articles/index.html',context)


def create(request):
  # POST 요청 => 데이터를 받아서 DB에 저장
  if request.method == 'POST':
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # Binding 과정
    # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다
    # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다
    form = ArticleForm(request.POST)
    #embed()
    if form.is_valid():
      # form이 dict형태로 바뀌어져서 들어옴
      # cleaned_data를 통해 디셔너리 안 데이터를 검증한다
      # 1. Form Class
      # title = form.cleaned_data.get('title')
      # content = form.cleaned_data.get('content')
      # article = Article.objects.create(title=title, content=content)
      # 2. Model Form Class
      article = form.save()
    return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
  
  # form으로 전달받는 형태가 2가지
  # 1. GET요청 -> 비어있는 폼 전달
  # 2. 유효성 검증 실패 -> 에러 메시지를 포함한 채로 폼 전달
  context = {'form':form }
  return render(request, 'articles/form.html', context)


def detail(request, article_pk):
  #article = Article.objects.get(pk=article_pk)
  article = get_object_or_404(Article, pk=article_pk)
  comment_form = CommentForm()
  comments = article.comment_set.all()
  context = {
    'article':article,
    'comment_form':comment_form,
    'comments':comments,
  }
  return render(request, 'articles/detail.html', context)


# post요청만 들어올때 require_post 사용가능
@require_POST
def delete(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  # if request.method == 'POST':
  #   article.delete()
  #   return redirect('articles:index')
  # else:
  #   return redirect('articles:detail', article.pk)
  article.delete()
  return redirect('articles:index')


def update(request, article_pk):
  article= get_object_or_404(Article, pk=article_pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      # article.title = form.cleaned_data('title')
      # article.content = form.cleaned_data('content')
      article = form.save()
      return redirect('articles:detail', article.pk)
  else:
    # form = ArticleForm(initial={
    #   'title':article.title,
    #   'content':article.content
    # })
    form = ArticleForm(instance=article)
    # 2가지 form 형식
    # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid가 False가 리턴됐을 때, 오류 메시지 포함해서 사용자에게 던져줌

    context = {
      'form':form, 
      'article':article 
    }
    #return render(request, 'articles/create.html', context)
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    # save() 메서드 -> 선택 인자 : (기본값) commit=True
    # comment의 article정보를 넣어줘야 하는데 정보가 없다면 일단 막아줘야한다
    # commit=False 하면 DB에 바로 저장되는 것을 막아준다. 객체 하나만 만들어진 상태
    comment = comment_form.save(commit=False)
    comment.article = article
    comment.save()
    return redirect('articles:detail', article.pk)



@require_POST
def comments_delete(request, article_pk, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  comment.delete()
  return redirect('articles:detail', article_pk)