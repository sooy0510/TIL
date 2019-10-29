from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
  name = '이수연'
  return render(request,'index.html',{'name':name})  


# 정보를 던져줄 페이지
def throw(request):
  return render(request, 'throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
def catch(request):
  # flask : request.args.getpyth
  message = request.GET.get('message')
  context = {'message' : message}
  return render(request,'catch.html',context)


# [실습] 아스키 아트 API를 통한 요청-응답 실습
# 사용자로부터 텍스트 입력받는 페이지
def art(request):
  return render(request,'art.html')

# 텍스트 받아서 아스키 아트로 보여주는 페이지
def result(request):
  # 1. 사용자가 입력한 Form 데이터를 가져온다.
  # request.GET : 사용자가 input을 통해 넘겨준 데이터가 dictionary 형태로 들어옴
  word = request.GET.get('word')

  # 2. ARTII API로 요청을 보내서, 응답 결과를 변수에 담는다. (폰트 정보들)
  fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

  # 3. 가져온 폰트들을 리스트 형태로 담는다.
  fonts = fonts.split('\n')

  # 4. 폰트 하나를 랜덤으로 선택한다.
  font = random.choice(fonts)

  # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
  result = requests.get(
    f'http://artii.herokuapp.com/make?text={word}&font={font}'
  ).text

  # 6. 최종 결과물을 사용자에게 리턴한다.
  context = {'result': result}

  return render(request, 'result.html', context)


# 회원가입 폼을 보여주는 페이지
def user_new(request):
  return render(request, 'user_new.html')

# 회원가입 요청을 처리하는 페이지(로직)
# 실제로는 이렇게 구현하지 않는다. 
def user_create(request):
  user_id = request.POST.get('user_id')
  pwd = request.POST.get('pwd')
  context = {
    'user_id' : user_id,
    'pwd' : pwd,
  }
  return render(request, 'user_create.html', context)