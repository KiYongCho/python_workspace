# day5_challenge_sol.py
# AI휴먼 과정 5일차 Challenge 과제 풀이

# 학생 이름을 Key, 점수를 Value로 저장합니다.
students = {
    "민수": 72,
    "지연": 88,
    "준호": 95,
    "서연": 61,
    "하늘": 84,
}

# 전체 점수 합계를 저장할 변수를 0으로 초기화합니다.
total = 0

# 합격자 수를 저장할 변수를 0으로 초기화합니다.
pass_count = 0

# 최고점 학생 이름을 저장할 변수를 빈 문자열로 초기화합니다.
top_name = ""

# 실제 점수보다 작은 값으로 최고점 초기값을 준비합니다.
top_score = -1

# 결과표 제목을 출력합니다.
print("학생 성적표")

# 결과 영역을 구분하기 위한 선을 출력합니다.
print("-" * 34)

# Dictionary에서 학생 이름과 점수를 하나씩 반복합니다.
for name, score in students.items():
    # 현재 점수를 전체 합계에 누적합니다.
    total += score

    # 현재 점수가 80점 이상인지 확인합니다.
    if score >= 80:
        # 합격자 수를 1 증가시킵니다.
        pass_count += 1

    # 현재 점수가 최고점보다 높은지 확인합니다.
    if score > top_score:
        # 최고점 값을 현재 점수로 교체합니다.
        top_score = score
        # 최고점 학생 이름도 현재 학생으로 교체합니다.
        top_name = name

    # 90점 이상인지 확인합니다.
    if score >= 90:
        # A 등급을 저장합니다.
        grade = "A"
    # 80점 이상인지 확인합니다.
    elif score >= 80:
        # B 등급을 저장합니다.
        grade = "B"
    # 70점 이상인지 확인합니다.
    elif score >= 70:
        # C 등급을 저장합니다.
        grade = "C"
    # 위 조건에 해당하지 않는 점수를 처리합니다.
    else:
        # D 등급을 저장합니다.
        grade = "D"

    # 80점 이상이면 PASS, 아니면 RETRY를 저장합니다.
    status = "PASS" if score >= 80 else "RETRY"

    # 학생별 결과를 한 줄로 출력합니다.
    print(f"{name} | {score}점 | {grade}등급 | {status}")

# 전체 학생 수를 계산합니다.
student_count = len(students)

# 전체 평균을 계산합니다.
average = total / student_count

# 학생별 결과와 전체 요약을 구분하는 선을 출력합니다.
print("-" * 34)

# 평균 점수를 소수점 둘째 자리까지 출력합니다.
print(f"평균: {average:.2f}")

# 합격자 수를 출력합니다.
print("합격자 수:", pass_count)

# 최고점 학생 이름과 점수를 출력합니다.
print(f"최고점: {top_name} / {top_score}점")
