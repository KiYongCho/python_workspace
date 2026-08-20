# 파이썬의 데이터 타입, csv 파일 입출력
import csv

# 1. 기본 데이터 타입

name = '김민수'       # 문자열, str
age = 30             # 정수, int
score = 4.5          # 실수, float
is_vip = True        # 불리언, bool

print(name, age, score, is_vip)
print(type(name), type(age), type(score), type(is_vip))

# 2. 리스트 데이터
# len: 5, index range: 0 ~ 4
sales = [120000, 150000, 98000, 175000, 132000] #sales는 5개위 정수를 갖고 있다

print(f'데이터 개수: {len(sales)}')
print(f'총계: {sum(sales)}')
print(f'평균: {sum(sales) / len(sales)}')
print(f'최고값: {max(sales)}')
print(f'최저값: {min(sales)}')

# 3. 리스트 + 딕셔너리

orders = [
    {'상품': '키보드', '수량': 2, '매출': 80000},
    {'상품': '마우스', '수량': 3, '매출': 75000},
    {'상품': '모니터', '수량': 1, '매출': 280000},
]

# 첫번째 상품의 수량
print(orders[0]['수량'])

# 세번재 상품의 매출
print(orders[2]['매출'])

# 전체상품 매출 합계 (반복문)
print(orders[0]['매출'] + orders[1]['매출'] + orders[2]['매출'])
total = 0
for order in orders: # 리스트내의 딕셔너리를 하나씩 꺼내가며 반복(반복문)
    total += order['매출'] # total 변수에 매출 누적, total = total + order['매출'], +=는 누계한다의미
print(total)

# 4. csv 저장

import csv

# 파일경로, w는 쓰기모드, newline='' windows에서 줄바꿈 방지, encoding='utf-8-sig'는 한글처리
with open('./assets/orders.csv', 'w', newline='', encoding='utf-8-sig') as f:
    # 컬럼명을 지정해서 각 행의 데이터를 딕셔너리를 씀
    writer = csv.DictWriter(f, fieldnames=['상품', '수량', '매출'])
    writer.writeheader() # 헤더 라인이 파일에 써짐
    writer.writerows(orders) #데이터 라인들이 파일에 써짐

# 5. csv 파일 읽기 + 총매출 계산

total=0

# 파일경로, 읽기모드, 한글처리
with open('./assets/orders.csv','r', encoding='utf-8-sig') as f:
    # CSV파일의 데이터들을 딕셔너리로 읽어오는 리더
    reader = csv.DictReader(f)
    for row in reader:  # 행의 수만큼 반복
        total += int(row['매출']) # 매출누적, 문자열이므로 정수int로 변환

print(f'총 매출: {total}')