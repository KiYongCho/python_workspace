# Series_ex.py
# pandas - Series

# https://pandas.pydata.org/docs/reference/api/pandas.Series.html

from common.common_util import p, scroll
import pandas as pd


# 딕셔너리 > 시리즈

dict_data = {'name': '홍길동', 'age': 20, 'gender': '남'}

sr = pd.Series(dict_data)
p(sr)
p(type(sr)) # <class 'pandas.Series'>


# 시리즈 > 딕셔너리

dict_data = sr.to_dict()
p(dict_data) # {'name': '홍길동', 'age': 20, 'gender': '남'}


# 리스트 > 시리즈

list_data = ['홍길동', 20, '남']

sr = pd.Series(list_data) # 숫자 인덱스로 생성됨
p(sr)
p(sr[0]) # 홍길동, 숫자 인덱스 1의 값
p(sr[1:2]) # 1 20, 숫자 인덱스 1의 값
p(sr[[1, 2]]) # 1 20 2 남, 숫자 인덱스 1~2의 값

sr = pd.Series(list_data, index=['name', 'age', 'gender']) # 문자 인덱스로 생성됨
p(sr)


# 시리즈 > 리스트

list_data = sr.to_list()
p(list_data) # ['홍길동', 20, '남']


# 시리즈 > JSON 문자열

json_str = sr.to_json()
p(json_str) # {"name":"\ud64d\uae38\ub3d9","age":20,"gender":"\ub0a8"}
p(type(json_str)) # <class 'str'>


# JSON 문자열 > 시리즈

import json
json_obj = json.loads(json_str)
sr = pd.Series(json_obj)
p(sr)


# 시리즈 속성

p(sr.index) # Index(['name', 'age', 'gender'], dtype='str'), 시리즈의 인덱스

p(sr.values) # ['홍길동' 20 '남'], 시리즈의 값

p(sr.dtype) # object, 시리즈 값의 타입

p(sr.shape) # (3,), 시리즈의 모양(형태)

p(sr.ndim) # 1, 시리즈의 차원

p(len(sr)) # 3, 시리즈 원소의 개수

p(sr['age']) # 20, 문자 인덱스 age의 값

p(type(sr['age'])) # <class 'int'>

p(sr['age':'gender']) # age 20 gender 남, 문자 인덱스 age와 gender의 값

p(type(sr['age':'gender'])) # <class 'pandas.Series'>

p(sr[['age', 'gender']]) # age 20 gender 남, 문자 인덱스 age와 gender의 값

p(type(sr[['age', 'gender']])) # <class 'pandas.Series'>


# 단일 원소 시리즈

p(pd.Series()) # Series([], dtype: object), 요소가 없는 시리즈

sr = pd.Series(10) # 스칼라 원소를 가지는 시리즈
p(sr) # 0 10

sr = pd.Series(10, index=['a', 'b', 'c'])
p(sr) # a 10 b 10 c 10

# 시리즈 연산
hongscore = pd.Series({'국어': 100, '영어': 90, '수학': 80, '과학': 70})
p(hongscore)

hongscore_reg = hongscore / 10
p(hongscore_reg)

kangscore = pd.Series({'국어': 80, '영어': 70, '수학': 60, '과학': 50})
p(kangscore)

score_add = hongscore + kangscore
score_sub = hongscore - kangscore
score_mul = hongscore * kangscore
score_div = hongscore / kangscore

p(score_add)
p(score_sub)
p(score_mul)
p(score_div)

score_result = pd.DataFrame(
    [score_add, score_sub, score_mul, score_div],
    index=['덧셈', '뺄셈', '곱셈', '나눗셈']
)
p(score_result)

import numpy as np

leescore = pd.Series({'국어': np.nan, '영어': 70, '수학': 60, '과학': np.nan})
p(leescore)

p(hongscore + leescore) # NaN과의 연산 결과는 NaN
p(hongscore - leescore)
p(hongscore * leescore)
p(hongscore / leescore) # NaN과의 연산 결과는 NaN

result_add = hongscore.add(leescore, fill_value=0) # NaN인 경우 0으로 연산
result_sub = hongscore.sub(leescore, fill_value=0)
result_mul = hongscore.mul(leescore, fill_value=0)
result_div = hongscore.div(leescore, fill_value=0) # NaN인 경우 0으로 연산

p(result_add)
p(result_sub)
p(result_mul)
p(result_div)

# 텍스트 처리
fruits = pd.Series(['Apple', 'Banana', 'Cherry'])
p(fruits)
p(type(fruits)) # str

fruits = pd.Series(['Apple', 'Banana', 'Cherry'], dtype=pd.StringDtype()) # 또는 dtype='string'
p(fruits)
p(type(fruits)) # string

ser = pd.Series(
    ['Apple_사과', 'Banana_바나나', 'Cherry_체리', np.nan],
    index=['First', ' Second ', ' Third ', 'Fourth']
)
p(ser)

p(ser.str.lower()) # 소문자로
p(ser.str.upper()) # 대문자로
p(ser.str.len()) # 길이

sp_ser = ser.str.split('_')
p(sp_ser)
p(type(sp_ser)) # <class 'pandas.Series'>

sp_ser2 = ser.str.split('_', expand=True) # 데이터프레임으로 확장 (리스트의 요소들을 컬럼으로 분할)
p(sp_ser2)
p(type(sp_ser2)) # <class 'pandas.DataFrame'>

p(sp_ser2.get(1)) # 컬럼인덱스 1

idx = ser.index
p(idx) # Index(['First', ' Second ', ' Third ', 'Fourth'], dtype='str')

p(idx.str.lstrip()) # 왼쪽 공백 제거
p(idx.str.rstrip()) # 오른쪽 공백 제거
p(idx.str.strip()) # 앞뒤 공백 제거

p(ser.str.replace('_', ':', regex=False)) # _를 :로 변환 (정규표현식 사용 않음)
p(ser.str.replace('[^a-zA-Z\\s]', '', regex=True)) # 영문자나 공백문자가 아니면 ''로 변환 (정규표현식 사용)

p(ser.str[0]) # 각 문자열의 첫번째 문자
p(ser.str[0:4]) # 각 문자열의 첫번째 문자메서 네번째 문자까지

p(ser.str.contains('A')) # A포함 여부 True/False 반환
p(ser.str.contains(r'[A|B][a-z]+')) # A나 B가 나오고 영문소문자가 하나이상 나옴

ser2 = pd.Series(
    ['a1', 'b2', 'c3', 'd4a5', 'e6e7', 'f8'],
    dtype='string'
)

ea = ser2.str.extractall(r'(\d)') # extractall(정규표현식) : 정규표현식에 매칭되는 모든 값을 추출
print(ea)
gb = ea.groupby(level=0) # groupby(level=0) : 시리즈의 인덱스로 그룹핑
print(gb)
digits = gb.agg(''.join) # 그룹핑 결과를 합침
p(digits)

p(ser2.str.replace(r'\D', '', regex=True)) # 위 코드의 간단버젼


scroll(15)



















