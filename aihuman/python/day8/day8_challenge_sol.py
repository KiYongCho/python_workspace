# day8_challenge_sol.py
# Day 8 Challenge 과제 풀이

# 학생 1명의 데이터와 기능을 담당하는 클래스를 정의합니다.
class Student:
    # 객체 생성 시 이름과 점수를 전달받습니다.
    def __init__(self, name, score):
        # 이름을 객체 속성으로 저장합니다.
        self.name = name
        # 점수를 객체 속성으로 저장합니다.
        self.score = score

    # 현재 학생의 합격 여부를 반환합니다.
    def grade(self):
        # 점수가 80점 이상이면 PASS를 반환합니다.
        if self.score >= 80:
            return "PASS"
        # 그 외에는 RETRY를 반환합니다.
        return "RETRY"

    # 현재 학생 정보를 보기 좋게 출력합니다.
    def show(self):
        # 이름, 점수, 합격 여부를 출력합니다.
        print(self.name, self.score, self.grade())


# 학생 객체 여러 개를 리스트에 저장합니다.
students = [
    Student("김민수", 85),
    Student("이서연", 92),
    Student("박지훈", 76),
    Student("정하늘", 88),
    Student("오세진", 69),
]

# 전체 학생 정보를 출력합니다.
print("[전체 학생]")
# 모든 학생 객체를 반복합니다.
for student in students:
    # 현재 학생 정보를 출력합니다.
    student.show()

# 합격 학생 제목을 출력합니다.
print("\n[합격 학생]")
# 합격 학생 수를 저장할 변수를 0으로 시작합니다.
pass_count = 0
# 점수 합계를 저장할 변수를 0으로 시작합니다.
total = 0

# 모든 학생 객체를 반복합니다.
for student in students:
    # 현재 학생의 점수를 합계에 누적합니다.
    total += student.score
    # 현재 학생이 PASS인지 확인합니다.
    if student.grade() == "PASS":
        # 합격 학생 정보를 출력합니다.
        student.show()
        # 합격 학생 수를 1 증가시킵니다.
        pass_count += 1

# 총점을 학생 수로 나누어 평균을 계산합니다.
average = total / len(students)
# 평균 점수를 소수점 첫째 자리까지 출력합니다.
print(f"\n전체 평균: {average:.1f}")
# 합격 학생 수를 출력합니다.
print(f"PASS 학생 수: {pass_count}")

# 결과 파일 저장 중 오류에 대비해 try 문을 사용합니다.
try:
    # UTF-8 인코딩으로 결과 파일을 쓰기 모드로 엽니다.
    with open("day8_challenge_result.txt", "w", encoding="utf-8") as file:
        # 전체 학생 객체를 반복합니다.
        for student in students:
            # 각 학생의 이름, 점수, 결과를 한 줄에 저장합니다.
            file.write(f"{student.name},{student.score},{student.grade()}\n")
        # 마지막 부분에 평균 점수를 저장합니다.
        file.write(f"평균,{average:.1f}\n")
        # 마지막 부분에 합격 학생 수를 저장합니다.
        file.write(f"PASS 학생 수,{pass_count}\n")
    # 파일 저장 성공 메시지를 출력합니다.
    print("결과를 day8_challenge_result.txt 파일에 저장했습니다.")
# 운영체제 수준의 파일 오류가 발생하면 실행합니다.
except OSError as error:
    # 오류 내용을 출력합니다.
    print(f"파일 저장 중 오류가 발생했습니다: {error}")
