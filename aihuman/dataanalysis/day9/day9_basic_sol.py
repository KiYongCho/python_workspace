# ============================================================
# AI휴먼 9일차 Basic 과제 풀이
# 주제: 고객센터 대기시간 1차원 배열 분석
# ============================================================

# NumPy 라이브러리를 np라는 별칭으로 불러옵니다.
import numpy as np

# 상담 대기시간 데이터를 1차원 NumPy 배열로 생성합니다.
wait_times = np.array([12, 8, 15, 6, 20, 9, 11, 7])

# 배열의 형태를 출력합니다.
print("shape:", wait_times.shape)

# 배열의 차원 수를 출력합니다.
print("ndim:", wait_times.ndim)

# 전체 원소 개수를 출력합니다.
print("size:", wait_times.size)

# 배열 원소의 자료형을 출력합니다.
print("dtype:", wait_times.dtype)

# 전체 대기시간의 합계를 계산합니다.
total_wait = wait_times.sum()

# 평균 대기시간을 계산합니다.
avg_wait = wait_times.mean()

# 가장 짧은 대기시간을 계산합니다.
min_wait = wait_times.min()

# 가장 긴 대기시간을 계산합니다.
max_wait = wait_times.max()

# 합계를 출력합니다.
print("합계:", total_wait)

# 평균을 출력합니다.
print("평균:", avg_wait)

# 최솟값을 출력합니다.
print("최솟값:", min_wait)

# 최댓값을 출력합니다.
print("최댓값:", max_wait)

# 평균보다 긴 대기시간만 조건 인덱싱으로 추출합니다.
long_waits = wait_times[wait_times > avg_wait]

# 평균보다 긴 대기시간을 출력합니다.
print("평균보다 긴 대기시간:", long_waits)

# 모든 대기시간을 2분씩 줄이는 벡터 연산을 수행합니다.
improved_wait_times = wait_times - 2

# 개선 후 전체 배열을 출력합니다.
print("개선 후 대기시간:", improved_wait_times)

# 개선 후 평균 대기시간을 계산합니다.
improved_avg = improved_wait_times.mean()

# 개선 후 평균을 출력합니다.
print("개선 후 평균:", improved_avg)
