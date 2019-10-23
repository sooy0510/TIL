# Python Dictionary

## 1. 기본기

### 1.1 딕셔너리 만들기

- 가장 많이 사용되는 자료형 + 웹 개발 하면서 마주칠 가능성이 가장 높음

- 딕셔너리는 기본적으로 key와 value 구조!

  - Key : `string`, `integer`, `float`, `boolean` 가능! 하지만 `list`, `dictionary`는 안된다.
  - Value : 모든 자료형 가능. `list`와 `dictionary`는

  ```python
  # 1. 딕셔너리 만들기
  lunch = {
    '중국집': '032'
  }
  lunch = dict(중국집='032')
  ```

  



### 1.2 딕셔너리 내용 추가하기

- 추가하기

  ```python
  # 2. 딕셔너리 내용 추가하기
  lunch['분식집'] = '031'
  ```

  

### 1.3 딕셔너리 내용 가져오기

- 내용 가져오기(2가지)

  ```python
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
  ```

  

### 1.4 딕셔너리 반복문 활용하기

- 반복문 활용

  ```python
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
  ```

  



### 1.5 연습문제

- dict_practice.py 참고



## 2. 실습 문제

- dict_practice2.py 참고

