from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#   title = forms.CharField(
#     # HTML tag 와 동일
#     max_length=30,
#     label='제목',
#     widget=forms.TextInput(
#       attrs={
#         'class':'title',
#         'placeholder':'제목을 입력해주세요..!',
#       }
#     )
#   )
#   # 비워둘 수 있다
#   content = forms.CharField(
#     label='내용',
#     # widget : Input Type 지정 -> Textarea / 알맞은 속성값 부여
#     widget=forms.Textarea(
#       attrs={
#         'class':'content',
#         'placeholder':'내용을 입력해주세요',
#         'rows':5,
#         'cols':30,
#       }
#     )
#   )


# ModelForm
# 1. ModelForm 클래스를 상속받아 사용한다
# 2. 메타데이터로 Model 정보를 건네주면, ModelForm이 자동으로 field에 맞춰
#   input을 생성해준다

class ArticleForm(forms.ModelForm):
  # custumizing(선택)
  title = forms.CharField(
    label='제목',
    max_length=10,
    widget=forms.TextInput(
      attrs={
        'class':'title',
        'placeholder':'제목 입력하세요..'
      }
    )
  )

  content = forms.CharField(
    label='내용',
    widget=forms.Textarea(
      attrs={
        'class':'content',
        'placeholder':'내용을 입력하세요',
        'rows':5,
        'cols':30,
      }
    )
  )


  # 메타데이터 -> 데이터의 데이터
  # ex) 사진 한장 (촬영장비이름, 촬영환경 등)
  class Meta:
    model = Article
    #fields = '__all__'
    fields = ('title','content',)




class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    # article 까지 넣어주면 사용자가 선택해서 바꿀수도 있음. 로직의 논리에 맞지 않는다!
    fields = ('content',)

 