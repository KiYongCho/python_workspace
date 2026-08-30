# day8_basic_sol.py
# Day 8 Basic 과제 풀이

# 학생 객체를 만들기 위한 Student 클래스를 정의합니다.
class Student:
    # 객체를 생성할 때 이름과 점수를 전달받습니다.
    def __init__(self, name, score):
        # 전달받은 이름을 객체의 name 속성에 저장합니다.
        self.name = name
        # 전달받은 점수를 객체의 score 속성에 저장합니다.
        self.score = score


# 첫 번째 Student 객체를 생성합니다.
student1 = Student("김민수", 85)
# 두 번째 Student 객체를 생성합니다.
student2 = Student("이서연", 92)

# 첫 번째 객체의 name과 score 속성을 출력합니다.
print(student1.name, student1.score)
# 두 번째 객체의 name과 score 속성을 출력합니다.
print(student2.name, student2.score)
