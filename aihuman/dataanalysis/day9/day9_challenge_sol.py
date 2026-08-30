# ============================================================
# AI휴먼 9일차 Challenge 과제 풀이
# 주제: 생산라인 불량 데이터 분석과 브로드캐스팅
# ============================================================

# NumPy 라이브러리를 np라는 별칭으로 불러옵니다.
import numpy as np

# 4개 생산라인의 6시간 불량 개수를 2차원 배열로 생성합니다.
defects = np.array([
    [3, 5, 4, 6, 2, 4],
    [6, 7, 5, 8, 6, 7],
    [2, 3, 1, 4, 3, 2],
    [4, 5, 6, 5, 7, 4]
])

# 각 라인의 평균 불량 개수를 axis=1로 계산합니다.
line_avg = defects.mean(axis=1)

# 라인별 평균을 출력합니다.
print("라인별 평균:", np.round(line_avg, 2))

# 각 시간대의 전체 불량 개수를 axis=0으로 계산합니다.
hour_total = defects.sum(axis=0)

# 시간대별 전체 불량 개수를 출력합니다.
print("시간대별 합계:", hour_total)

# 각 라인의 시간당 목표 불량 개수를 1차원 배열로 생성합니다.
target = np.array([4, 5, 3, 4])

# np.newaxis를 이용해 목표값을 4행 1열 형태로 변경합니다.
target_column = target[:, np.newaxis]

# 변경된 목표값 배열의 shape를 출력합니다.
print("목표 shape:", target_column.shape)

# 실제 불량 개수에서 각 라인의 목표값을 뺍니다.
difference = defects - target_column

# 목표 대비 차이 배열을 출력합니다.
print("목표 대비 차이:\n", difference)

# 실제 불량 개수가 라인별 목표값보다 큰 위치를 Boolean 배열로 만듭니다.
over_target = defects > target_column

# 목표 초과 여부를 출력합니다.
print("목표 초과 여부:\n", over_target)

# 각 행의 True 개수를 더하여 라인별 목표 초과 횟수를 계산합니다.
over_count = over_target.sum(axis=1)

# 라인별 목표 초과 횟수를 출력합니다.
print("라인별 목표 초과 횟수:", over_count)

# 목표 초과 횟수가 가장 많은 라인의 인덱스를 찾습니다.
worst_line_index = np.argmax(over_count)

# 가장 많은 초과가 발생한 라인 인덱스를 출력합니다.
print("최다 초과 라인 인덱스:", worst_line_index)

# 각 라인의 최솟값을 구하고 4행 1열 형태로 유지합니다.
line_min = defects.min(axis=1)[:, np.newaxis]

# 각 라인의 최댓값을 구하고 4행 1열 형태로 유지합니다.
line_max = defects.max(axis=1)[:, np.newaxis]

# 라인별 최솟값 배열의 shape를 출력합니다.
print("라인별 최솟값 shape:", line_min.shape)

# 라인별 최댓값 배열의 shape를 출력합니다.
print("라인별 최댓값 shape:", line_max.shape)

# Min-Max 정규화 공식의 분모를 계산합니다.
range_value = line_max - line_min

# 브로드캐스팅으로 각 라인 내부의 값을 0~1 범위로 정규화합니다.
normalized = (defects - line_min) / range_value

# 정규화 결과를 소수점 둘째 자리까지 반올림하여 출력합니다.
print("라인별 Min-Max 정규화:\n", np.round(normalized, 2))
