# day8_application_sol.py
# Day 8 Application 과제 풀이

# 학생 데이터와 학생 관련 기능을 묶기 위한 클래스를 정의합니다.
class Student:
    # 객체를 만들 때 이름과 점수를 초기화합니다.
    def __init__(self, name, score):
        # 이름을 객체의 속성에 저장합니다.
        self.name = name
        # 점수를 객체의 속성에 저장합니다.
        self.score = score

    # 합격 여부를 계산하는 메서드입니다.
    def grade(self):
        # 현재 객체의 점수가 80점 이상인지 확인합니다.
        if self.score >= 80:
            # 80점 이상이면 PASS를 반환합니다.
            return "PASS"
        # 80점 미만이면 아래 값을 반환합니다.
        return "RETRY"

    # 학생 정보를 한 줄에 출력하는 메서드입니다.
    def show(self):
        # grade() 메서드의 결과를 함께 출력합니다.
        print(f"이름: {self.name}, 점수: {self.score}, 결과: {self.grade()}")


# 여러 Student 객체를 생성해서 리스트에 바로 저장합니다.
students = [
    Student("김민수", 85),
    Student("이서연", 92),
    Student("박지훈", 76),
    Student("정하늘", 88),
]

# 리스트에 저장된 학생 객체를 하나씩 꺼냅니다.
for student in students:
    # 현재 학생의 show() 메서드를 실행합니다.
    student.show()
