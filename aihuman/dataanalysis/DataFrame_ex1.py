# DataFrame_ex1.py
# pandas - DataFrame 1

from common.common_util import p, scroll
import pandas as pd

# 딕셔너리 > 데이터프레임
dict_data = {
    'name': ['홍길동', '강감찬', '유관순'],
    'age': [30, 40, 20],
    'gender': ['male', 'male', 'female']
}
p(dict_data)
p(type(dict_data)) # <class 'dict'>
df = pd.DataFrame(dict_data)
p(df)
p(type(df)) # <class 'pandas.DataFrame'>

# 행인덱스 / 열이름 설정
list_data = [
    ['홍길동', 40, 'male'],
    ['강감찬', 30, 'male'],
    ['유관순', 20, 'female']
]
df = pd.DataFrame(
    list_data,
    index=['p1', 'p2', 'p3'], # 행인덱스
    columns=['이름', '나이', '성별'] # 열이름
)
p(df)

# 행인덱스 / 열이름
p(df.index) # Index(['p1', 'p2', 'p3'], dtype='str')
p(df.columns) # Index(['이름', '나이', '성별'], dtype='str')

# index, columns 변경
df.index = ['person1', 'person2', 'person3']
df.columns = ['성명', '연령', '남여구분']
p(df)
df = df.rename(index={'person1': 'p1', 'person2': 'p2', 'person3': 'p3'})
df = df.rename(columns={'성명': '이름', '연령': '나이', '남여구분': '성별'})
p(df)

# 행/열 삭제
df2 = df.copy() # 데이터프레임 복제
df2 = df2.drop('p1') # 행인덱스 p1행 삭제
p(df2)
# 행인덱스 p2행과 p3행 삭제, axis=0 행, axis=1 열
df2 = df2.drop(['p2', 'p3'], axis=0)
p(df2)

df3 = df.copy()
# 행인덱스 p1행과 p2행 삭제, axis='index' 행, axis='columns' 열
df3 = df3.drop(['p1', 'p2'], axis='index')
p(df3)
df3 = df3.drop(index=['p3']) # 행인덱스 p3행 삭제
p(df3)

df4 = df.copy()
df4 = df4.drop(['나이'], axis=1)
p(df4)
df4 = df4.drop(['이름', '성별'], axis=1)
p(df4)

df5 = df.copy()
df5 = df5.drop(['나이'], axis='columns') # df5 = df5.drop(columns='나이')
p(df5)
df5 = df5.drop(['이름', '성별'], axis='columns')
p(df5)

# 단일 행 선택
p1 = df.loc['p1']
p(p1)
p(type(p1)) # <class 'pandas.Series'>
p2 = df.iloc[1]
p(p2)
p(type(p2)) # <class 'pandas.Series'>

# 다중 행 선택
p23 = df.loc[['p1', 'p2']] # 행인덱스 이름 접근
p(p23)
p(type(p23)) # <class 'pandas.DataFrame'>
p23 = df.iloc[[0, 1]] # 행인덱스 번호 접근
p(p23)
p23 = df.iloc[0:2] # 행인덱스 범위 접근
p(p23)

# 단일 열 선택
name = df['이름']
p(name)
p(type(name)) # <class 'pandas.Series'>
age = df.이름
p(age)
p(type(name)) # <class 'pandas.Series'>

# 다중 열 선택
nameage = df[['이름', '나이']]
p(nameage)
p(type(nameage)) # <class 'pandas.DataFrame'>
nameage = df.iloc[0:2]
p(nameage)
p(type(nameage)) # <class 'pandas.DataFrame'>

# 인덱스 변경
df = df.set_index('이름') # 인덱스를 '이름'으로 변경, 기존 인덱스 사라짐
p(df)

# 단일 원소 선택
hongage = df.loc['홍길동', '나이']
p(hongage)
p(type(hongage)) # <class 'numpy.int64'>
kaneage = df.iloc[1, 0] # 1행 0열
p(kaneage)
p(type(kaneage)) # <class 'numpy.int64'>

# 다중 원소 선택
hongagegender = df.loc['홍길동', ['나이', '성별']]
p(hongagegender)
p(type(hongagegender)) # <class 'pandas.Series'>
kangnameage = df.loc[['강감찬', '유관순'], ['나이', '성별']]
p(kangnameage)
p(type(kangnameage))
hongagegender = df.iloc[0, [0, 1]]
p(hongagegender)
p(type(hongagegender))
kangyounameage = df.iloc[[1, 2], [0, 1]]
p(kangyounameage)
p(type(kangyounameage))

# 열 추가
df['주소'] = '역삼동'
p(df)
df['주소'] = ['역삼동', '논현동', '수서동'] # 변경
p(df)
df['이메일'] = ['hong@hong.com', 'kang@kang.com', 'you@you.com'] # 추가
p(df)

# 행 추가
df.loc['이순신'] = [60, 'male', '도곡동', 'lee@lee.com']
p(df)

# 원소 변경
df.loc['홍길동', '나이'] = 45
p(df)
df.iloc[1, 2] = '여의도동'
p(df)
df.loc['홍길동', ['주소', '이메일']] = '풍납동', 'hong2@hong2.com'
p(df)

# 행/열 위치 변경
df2 = df.copy()
df2 = df2.transpose()
p(df2)

# 인덱스 초기화
df = df.reset_index()
#df = df.reset_index(drop=True) # 기존 인덱스 삭제
p(df)

# 인덱스 설정
df3 = df.copy()
df3 = df3.set_index('이름')
p(df3)
df3 = df3.set_index('이메일', append=True) # 인덱스 추가
p(df3)
df3 = df3.reset_index()
df3 = df3.set_index(['이름', '주소']) # 인덱스 변경 (멀티 열)
p(df3)

# 인덱스 재배열
df3 = df3.reset_index()
p(df3)
df3 = df3.reindex([0, 1, 2, 3, 4])
p(df3)
df3 = df3.fillna('미정') # NaN을 '미정'으로 변경
p(df3)

# 데이터프레임 정렬
df4 = df.copy()
p(df4)
df4 = df4.sort_index() # 행인덱스 기준 오름차순 정렬
p(df4)
df4 = df4.sort_index(ascending=False) # 행인덱스 기준 내림차순 정렬
p(df4)
df4 =df4.sort_values(by='나이') # 열의 값 기준 오름차순 정렬
p(df4)
df4 = df4.sort_values(by='나이', ascending=False) # 열의 값 기준 내림차순 정렬
p(df4)
df4.loc[4] = ['홍길동', 20, 'male', '양재동', 'hong3@hong3.com']
df4 = df4.sort_values(by=['이름', '나이'], ascending=False) # 열의 값 기준 내림차순 정렬 (2차 정렬)
p(df4)
# 첫번째 열의 값 기준 내림차순, 두번째 열의 값 기준 오름차순 정렬 (2차 정렬)
df4 = df4.sort_values(by=['이름', '나이'], ascending=[False, True])
p(df4)



scroll(15)



















































