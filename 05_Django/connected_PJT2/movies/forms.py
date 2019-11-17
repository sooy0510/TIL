from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
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

  description = forms.CharField(
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
  # 메타데이터로 Model 정보를 건네주면 , ModelForm이 자동으로 input태그를 생성해준다
  # ex) 사진 한장 (촬영장비이름, 촬영환경 등)
  class Meta:
    model = Movie
    #fields = '__all__'
    fields = ('title','description','poster',)
  