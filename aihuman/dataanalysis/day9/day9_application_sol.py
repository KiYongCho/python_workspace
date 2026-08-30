# ============================================================
# AI휴먼 9일차 Application 과제 풀이
# 주제: 2차원 NumPy 배열로 매장 매출 분석
# ============================================================

# NumPy 라이브러리를 np라는 별칭으로 불러옵니다.
import numpy as np

# 4개 매장의 5일 매출 데이터를 2차원 배열로 생성합니다.
sales = np.array([
    [120, 135, 128, 142, 150],
    [98, 105, 110, 115, 120],
    [160, 155, 172, 168, 180],
    [130, 125, 140, 138, 145]
])

# 배열의 shape를 출력합니다.
print("shape:", sales.shape)

# 배열의 전체 원소 개수를 출력합니다.
print("size:", sales.size)

# axis=1로 각 행, 즉 매장별 평균을 계산합니다.
store_avg = sales.mean(axis=1)

# 매장별 평균을 소수점 둘째 자리까지 반올림하여 출력합니다.
print("매장별 평균:", np.round(store_avg, 2))

# axis=0으로 각 열, 즉 요일별 매출 합계를 계산합니다.
day_total = sales.sum(axis=0)

# 요일별 매출 합계를 출력합니다.
print("요일별 합계:", day_total)

# 매장별 평균 중 가장 큰 값의 인덱스를 찾습니다.
best_store_index = np.argmax(store_avg)

# 평균 매출이 가장 높은 매장의 인덱스를 출력합니다.
print("최고 평균 매장 인덱스:", best_store_index)

# 전체 매출 평균을 계산합니다.
overall_avg = sales.mean()

# 전체 매출 평균을 출력합니다.
print("전체 평균:", round(float(overall_avg), 2))

# 전체 평균의 110%에 해당하는 기준값을 계산합니다.
high_threshold = overall_avg * 1.10

# 기준값을 출력합니다.
print("110% 기준값:", round(float(high_threshold), 2))

# 기준값 이상인 매출만 조건 인덱싱으로 추출합니다.
high_sales = sales[sales >= high_threshold]

# 기준값 이상인 매출을 출력합니다.
print("기준 이상 매출:", high_sales)

# 기준값 이상인 원소의 행·열 위치를 찾습니다.
row_indices, col_indices = np.where(sales >= high_threshold)

# 해당 값들의 행 인덱스를 출력합니다.
print("행 인덱스:", row_indices)

# 해당 값들의 열 인덱스를 출력합니다.
print("열 인덱스:", col_indices)
