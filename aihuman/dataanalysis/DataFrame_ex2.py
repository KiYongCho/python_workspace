# DataFrame_ex2.py
# pandas - DataFrame 2

from common.common_util import p, scroll
import pandas as pd
import seaborn as sns
import numpy as np

# seaborn의 타이타닉 데이터셋

titanic = sns.load_dataset("titanic") # seaboran의 titanic 데이터셋 로드
df = titanic.loc[:, ['age', 'fare']]
p(df)
p(type(df)) # <class 'pandas.DataFrame'>

# 데이터프레임 연산

addition = df + 10
p(addition)
p(type(addition))

result_add = df.add(addition, fill_value=0)
result_sub = df.sub(addition, fill_value=0)
result_mul = df.mul(addition, fill_value=0)
result_div = df.div(addition, fill_value=0)
# 나눗셈 결과과 inf 또는 -inf인 경우 NaN 처리
result_div = result_div.replace([np.inf, -np.inf], np.nan)

p(result_add)
p(result_sub)
p(result_mul)
p(result_div)

# 불리언 필터링

p(df[df['age']<=20]) # 나이 20이하
p(df['age']<=20) # 불리언 결과
p(df[~(df['age']<=20)]) # 나이 20이하 아님
p(~(df['age']<=20)) # 불리언 결과 (부정)
p(df[df['fare']>=30]) # 요금 30이상
p(df[(df['age']<=20) & (df['fare']>=30)]) # 나이 20이하 이면서 요금 30이상
p(df[(df['age']<=20) | (df['fare']>=30)]) # 나이 20이하 이거나 요금 30이상
mask = (titanic['age']<=20) | (titanic['fare']>=30) # 조건
p(titanic.loc[mask, ['age', 'fare', 'sex', 'alone']]) # 조건을 충족하는 컬럼 추출

# query() : 행 조건

p(df.query('age<=20')) # 나이 20이하
p(df.query('age<=20 and fare<=15')) # 나이 20이하 이면서 요금 15이하
p(df.query('age<=20 or fare<=15')) # 나이 20이하 이거나 요금 15이하

# isin()
town_filter = titanic['embark_town'].isin(['Southampton', 'Queenstown'])
df_town = titanic[town_filter]
p(df_town)

scroll(15)
























