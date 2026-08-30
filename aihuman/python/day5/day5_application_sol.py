# day5_application_sol.py
# AI휴먼 과정 5일차 Application 과제 풀이

# 분석할 점수 목록을 리스트로 준비합니다.
scores = [72, 88, 95, 61, 83, 90]

# 전체 합계를 저장할 변수를 0으로 초기화합니다.
total = 0

# 합격자 수를 저장할 변수를 0으로 초기화합니다.
pass_count = 0

# 첫 번째 점수를 현재 최고점으로 저장합니다.
highest = scores[0]

# 리스트의 점수를 하나씩 반복합니다.
for score in scores:
    # 현재 점수를 전체 합계에 누적합니다.
    total += score

    # 현재 점수가 80점 이상인지 확인합니다.
    if score >= 80:
        # 합격 조건을 만족하면 합격자 수를 1 증가시킵니다.
        pass_count += 1

    # 현재 점수가 저장된 최고점보다 큰지 확인합니다.
    if score > highest:
        # 더 큰 점수를 발견하면 최고점을 현재 점수로 교체합니다.
        highest = score

# 리스트의 원소 개수로 전체 학생 수를 구합니다.
student_count = len(scores)

# 합계를 학생 수로 나누어 평균을 계산합니다.
average = total / student_count

# 전체 학생 수를 출력합니다.
print("전체 학생 수:", student_count)

# 점수 합계를 출력합니다.
print("점수 합계:", total)

# 평균 점수를 소수점 둘째 자리까지 출력합니다.
print(f"평균 점수: {average:.2f}")

# 합격자 수를 출력합니다.
print("합격자 수:", pass_count)

# 최고점을 출력합니다.
print("최고점:", highest)
