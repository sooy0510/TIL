'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
s = sum(score.values())
print(f'평균은 {s/len(score.keys())}입니다')


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '수연': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '선아': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
s = 0
cnt = 0
for score_list in scores.values():
  for score in score_list.values():
    s += score
    cnt += 1

print(f'반 평균은 {s/cnt}점 입니다')



# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''

for key,values in cities.items():
  print(f'{key} : {sum(values)/len(values)}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
cold = 0
hot = 0
count = 0
hot_city = ""
cold_city = ""

for name, temp in cities.items():
    # 첫 번째 시행
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0: # 첫번째 시행을 위한 처리 
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot보다 더 더우면, hot에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(hot_city)
print(cold_city)


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in cities.get('서울'):
  print('있습니다')
else:
  print('없습니다')
