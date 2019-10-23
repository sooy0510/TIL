from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)

@app.route('/')
def hello():
  #return 'Hello World'
  return render_template('index.html')

@app.route('/sooy')
def sooy():
  return '수연이다!'

@app.route('/html')
def html():
  return '<h1>태그 사용가능</h1>'

@app.route('/html_multiline')
def html_multiline():
  return """
  <ol>
    <li>하이하이</li>
  </ol>
  """

# 동적 라우팅(Variable Routing)
@app.route('/greeting/<string:name>')
def greeting(name):
  #return f'반가워요, {name}'
  #사용자로부터 이름을 넘겨받고 rendering하고자 하는 html에서 지정한 이름으로 사용가능
  return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:num>')
def cube(num):
  result = num**3
  return render_template('cube.html', num=num, result=result)


@app.route('/movies')
def movies():
  movie_list = ['82년생김지영','조커','엔드게임','궁예']
  return render_template('movies.html', movies=movie_list)


# ping : 사용자로부터 입력을 받을 Form 페이지를 넘겨준다.
@app.route('/ping')
def ping():
  return render_template('ping.html')

# pong : 사용자로부터 Form 데이터를 전달받아서 가공한다.
@app.route('/pong')
def pong():
  user_name = request.args.get('user_name')
  return render_template('pong.html', user_name = user_name)


# fake naver
@app.route('/naver')
def naver():
  return render_template('naver.html')


# vonvon - ping
@app.route('/vonvon')
def vonvon():
  return render_template('vonvon.html')

# vonvon - pong
@app.route('/godmademe')
def godmademe():
  # 1. 사용자가 입력한 데이터를 가져온다.
  user_name = request.args.get('user_name')

  # 2. 사용자에게 보여줄 여러가지 재밌는 특성들 리스트를 만든다.
  first_list = ['잘생김','못생김','쭈꾸미','감자','존잘탱','반건조오징어','고구마말랭이']
  second_list = ['안경','빵모자','냄새','팔토시','소라게']
  third_list = ['허세','식욕','물욕','똘기','더러움']

  # 3. 리스트에서 랜덤으로 하나씩을 선택한다.
  face = random.choice(first_list)
  hobby = random.choice(second_list)
  food = random.choice(third_list)

  # 4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다.
  return render_template('godmademe.html', user_name=user_name, face=face, hobby=hobby, food=food)


# 1. 사용자로부터 임의의 텍스트를 입력받아서, 아스키 아트로 변환해서 돌려준다.
# 이때, 아스키 아트 폰트는 랜덤으로 하나를 지정해서 변환한다.

@app.route('/artiIn')
def artiIn():
  return render_template('artiiIn.html')
  
@app.route('/artiiOut')
def artiiOut():
  # 1. 사용자가 입력한 Form 데이터를 가져온다.
  word = request.args.get('word')

  # 2. ARTII API로 요청을 보내서, 응답 결과를 변수에 담는다. (폰트 정보들)
  fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

  # 3. 가져온 폰트들을 리스트 형태로 담는다.
  fonts = fonts.split('\n')

  # 4. 폰트 하나를 랜덤으로 선택한다.
  font = random.choice(fonts)

  # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
  result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

  # 6. 최종 결과물을 사용자에게 리턴한다.
  return render_template('artiiOut.html', result=result)
  
# end of file !!!!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다
if __name__ == '__main__':
  app.run(debug=True)