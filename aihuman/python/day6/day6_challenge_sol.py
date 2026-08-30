# day6_challenge_sol.py
# AI휴먼 day6 Challenge 과제 풀이

# 여러 학생의 이름과 점수 목록을 리스트 안의 딕셔너리로 저장합니다.
students = [
    # 첫 번째 학생 정보입니다.
    {"name": "김민수", "scores": [85, 90, 78]},
    # 두 번째 학생 정보입니다.
    {"name": "이서연", "scores": [95, 92, 92]},
    # 세 번째 학생 정보입니다.
    {"name": "박준호", "scores": [70, 68, 68]},
    # 네 번째 학생 정보입니다.
    {"name": "최지우", "scores": [82, 88, 91]}
]

# 점수 리스트를 받아 평균을 반환하는 함수를 정의합니다.
def get_average(scores):
    # 점수 합계를 저장할 변수를 0으로 초기화합니다.
    total = 0
    # scores 리스트의 각 점수를 반복합니다.
    for score in scores:
        # 현재 점수를 total에 누적합니다.
        total += score
    # 누적 합계를 점수 개수로 나누어 평균을 반환합니다.
    return total / len(scores)

# 점수를 받아 등급을 반환하는 함수를 정의합니다.
def get_grade(score):
    # 90점 이상인지 확인합니다.
    if score >= 90:
        # 조건을 만족하면 A를 반환합니다.
        return "A"
    # 80점 이상인지 확인합니다.
    elif score >= 80:
        # 조건을 만족하면 B를 반환합니다.
        return "B"
    # 70점 이상인지 확인합니다.
    elif score >= 70:
        # 조건을 만족하면 C를 반환합니다.
        return "C"
    # 60점 이상인지 확인합니다.
    elif score >= 60:
        # 조건을 만족하면 D를 반환합니다.
        return "D"
    # 위 조건을 모두 만족하지 않는 경우입니다.
    else:
        # F를 반환합니다.
        return "F"

# 학생 한 명의 출력용 리포트 문자열을 만드는 함수를 정의합니다.
def make_report(student):
    # 현재 학생의 점수 리스트로 평균을 계산합니다.
    average = get_average(student["scores"])
    # 계산된 평균을 이용하여 등급을 구합니다.
    grade = get_grade(average)
    # 학생 이름, 평균, 등급을 포함한 문자열을 반환합니다.
    return f"{student['name']} | 평균: {average:.1f} | 등급: {grade}"

# 전체 학생 평균을 계산하는 함수를 정의합니다.
def get_class_average(student_list):
    # 학생별 평균의 합을 저장할 변수를 0으로 초기화합니다.
    total_average = 0
    # student_list의 학생 정보를 하나씩 반복합니다.
    for student in student_list:
        # 현재 학생의 점수 리스트로 개인 평균을 계산합니다.
        average = get_average(student["scores"])
        # 현재 학생의 평균을 누적합니다.
        total_average += average
    # 학생 평균의 합을 학생 수로 나누어 전체 평균을 반환합니다.
    return total_average / len(student_list)

# students 리스트의 학생 정보를 하나씩 반복합니다.
for student in students:
    # 현재 학생의 리포트 문자열을 함수로 생성합니다.
    report = make_report(student)
    # 생성된 리포트 문자열을 출력합니다.
    print(report)

# 전체 학생 평균을 계산합니다.
class_average = get_class_average(students)

# 전체 학생 평균을 소수점 첫째 자리까지 출력합니다.
print(f"전체 학생 평균: {class_average:.1f}")
