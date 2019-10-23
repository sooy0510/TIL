# 1. 딕셔너리 만들기
lunch = {
  '중국집': '032'
}
lunch = dict(중국집='032')

# 2. 딕셔너리 내용 추가하기
lunch['분식집'] = '031'

# 3. 딕셔너리 내용 가져오기(2가지)
artists = {
  '아티스트':{
    '헤이즈' : '만추',
    '악동뮤지션' : "물 만난 물고기"
  }
}

# 헤이즈의 대표곡은?
print(artists['아티스트']['헤이즈'])
print(artists.get('아티스트').get('헤이즈'))

# 1.4딕셔너리 반복문 활용하기
# 1.4.1 기본 활용
for key in lunch:
  print(key)          # key 출력됨
  print(lunch[key])   # key로 value 추출

# 1.4.2 .items : Key, Value 모두 가져오기
for key, value in lunch.items():
  print(key,value)

# 1.4.3 .values : Value만 가져오기
for value in lunch.values():
  print(value)
  #=> 031,032

# 1.4.4. .keys : Key만 가져오기
for key in lunch.keys():
  print(key)
  #=> 중국집,분식집