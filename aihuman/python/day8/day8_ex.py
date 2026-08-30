# day8_ex.py
# Day 8 - 클래스와 객체를 활용한 학생 성적 관리 미니 프로그램

# 학생 1명의 데이터와 기능을 묶기 위해 Student 클래스를 정의합니다.
class Student:
    # 객체를 만들 때 자동으로 실행되는 초기화 메서드입니다.
    def __init__(self, name, score):
        # 전달받은 이름을 현재 객체의 name 속성에 저장합니다.
        self.name = name
        # 전달받은 점수를 현재 객체의 score 속성에 저장합니다.
        self.score = score

    # 현재 학생의 합격 여부를 문자열로 반환하는 메서드입니다.
    def grade(self):
        # 점수가 80점 이상인지 확인합니다.
        if self.score >= 80:
            # 80점 이상이면 PASS를 반환합니다.
            return "PASS"
        # 위 조건을 만족하지 않으면 아래 문장을 실행합니다.
        else:
            # 80점 미만이면 RETRY를 반환합니다.
            return "RETRY"

    # 현재 학생의 정보를 보기 좋게 출력하는 메서드입니다.
    def show(self):
        # grade() 메서드를 호출해 합격 여부를 함께 출력합니다.
        print(f"이름: {self.name}, 점수: {self.score}, 결과: {self.grade()}")


# 여러 학생의 전체 정보를 출력하는 함수를 정의합니다.
def show_all_students(students):
    # 구분용 제목을 출력합니다.
    print("\n[전체 학생]")
    # 학생 객체가 들어 있는 리스트를 처음부터 끝까지 반복합니다.
    for student in students:
        # 현재 학생 객체의 show() 메서드를 호출합니다.
        student.show()


# 합격한 학생만 출력하는 함수를 정의합니다.
def show_pass_students(students):
    # 구분용 제목을 출력합니다.
    print("\n[합격 학생]")
    # 학생 객체 리스트를 반복합니다.
    for student in students:
        # 현재 학생의 grade() 결과가 PASS인지 확인합니다.
        if student.grade() == "PASS":
            # PASS인 학생만 화면에 출력합니다.
            student.show()


# 학생들의 평균 점수를 계산하는 함수를 정의합니다.
def get_average(students):
    # 점수 합계를 저장할 변수를 0으로 시작합니다.
    total = 0
    # 모든 학생 객체를 반복합니다.
    for student in students:
        # 현재 학생의 점수를 total에 누적합니다.
        total += student.score
    # 총점을 학생 수로 나눈 평균을 반환합니다.
    return total / len(students)


# 학생 정보를 텍스트 파일로 저장하는 함수를 정의합니다.
def save_report(students, filename):
    # 파일 작업 중 오류가 발생할 수 있으므로 try 문을 사용합니다.
    try:
        # UTF-8 인코딩으로 텍스트 파일을 쓰기 모드로 엽니다.
        with open(filename, "w", encoding="utf-8") as file:
            # 결과 파일의 제목을 작성합니다.
            file.write("[학생 성적 결과]\n")
            # 모든 학생 객체를 반복합니다.
            for student in students:
                # 한 학생의 정보를 한 줄 문자열로 만듭니다.
                line = f"{student.name},{student.score},{student.grade()}\n"
                # 만든 문자열을 파일에 저장합니다.
                file.write(line)
            # 평균 점수를 계산해 파일 마지막에 저장합니다.
            file.write(f"평균,{get_average(students):.1f}\n")
        # 파일 저장이 정상적으로 끝났음을 안내합니다.
        print(f"\n결과가 {filename} 파일에 저장되었습니다.")
    # 파일 입출력 과정에서 오류가 발생하면 실행합니다.
    except OSError as error:
        # 발생한 오류 정보를 사용자에게 보여줍니다.
        print(f"파일 저장 중 오류가 발생했습니다: {error}")


# 프로그램의 전체 실행 흐름을 main() 함수로 묶습니다.
def main():
    # Student 클래스를 사용해 첫 번째 학생 객체를 생성합니다.
    student1 = Student("김민수", 85)
    # 두 번째 학생 객체를 생성합니다.
    student2 = Student("이서연", 92)
    # 세 번째 학생 객체를 생성합니다.
    student3 = Student("박지훈", 76)
    # 네 번째 학생 객체를 생성합니다.
    student4 = Student("정하늘", 88)

    # 생성한 학생 객체들을 하나의 리스트에 저장합니다.
    students = [student1, student2, student3, student4]

    # 모든 학생 정보를 출력합니다.
    show_all_students(students)
    # 합격 학생만 출력합니다.
    show_pass_students(students)

    # 평균 점수를 계산한 결과를 변수에 저장합니다.
    average = get_average(students)
    # 평균 점수를 소수점 첫째 자리까지 출력합니다.
    print(f"\n전체 평균: {average:.1f}")

    # 학생 성적 결과를 텍스트 파일로 저장합니다.
    save_report(students, "day8_result.txt")


# 이 파일을 직접 실행했을 때만 main() 함수를 호출합니다.
if __name__ == "__main__":
    # 프로그램의 시작 지점입니다.
    main()
