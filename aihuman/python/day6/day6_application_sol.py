# day6_application_sol.py
# AI휴먼 day6 Application 과제 풀이

# 학생 이름과 점수를 딕셔너리로 저장합니다.
students = {
    # 김민수 학생의 점수입니다.
    "김민수": 87,
    # 이서연 학생의 점수입니다.
    "이서연": 95,
    # 박준호 학생의 점수입니다.
    "박준호": 73,
    # 최지우 학생의 점수입니다.
    "최지우": 61,
    # 정하늘 학생의 점수입니다.
    "정하늘": 55
}

# 점수를 받아 등급을 반환하는 함수를 정의합니다.
def get_grade(score):
    # 점수가 90점 이상인지 확인합니다.
    if score >= 90:
        # 90점 이상이면 A를 반환합니다.
        return "A"
    # 점수가 80점 이상인지 확인합니다.
    elif score >= 80:
        # 80점 이상 90점 미만이면 B를 반환합니다.
        return "B"
    # 점수가 70점 이상인지 확인합니다.
    elif score >= 70:
        # 70점 이상 80점 미만이면 C를 반환합니다.
        return "C"
    # 점수가 60점 이상인지 확인합니다.
    elif score >= 60:
        # 60점 이상 70점 미만이면 D를 반환합니다.
        return "D"
    # 위 조건을 모두 만족하지 않는 경우입니다.
    else:
        # 60점 미만이면 F를 반환합니다.
        return "F"

# students 딕셔너리의 이름과 점수를 하나씩 반복합니다.
for name, score in students.items():
    # 현재 학생의 점수를 함수에 전달하여 등급을 구합니다.
    grade = get_grade(score)
    # 학생 이름, 점수, 등급을 한 줄로 출력합니다.
    print(f"{name} | {score}점 | {grade}등급")
