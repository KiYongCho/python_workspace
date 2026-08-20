# day2_basic_sol.py
# AI휴먼 과정 Day 2 Basic 과제 풀이입니다.
# 목표: 기본 변수를 만들고 f-string과 type()으로 출력합니다.

course_name = "AI휴먼"  # 과정명은 글자 데이터이므로 str 자료형의 문자열로 저장합니다.
name = "홍길동"  # 자신의 이름을 문자열로 저장합니다.
age = 22  # 나이는 숫자 데이터이므로 int 자료형의 정수로 저장합니다.
desired_job = "AI 개발자"  # 희망직무는 글자 데이터이므로 문자열로 저장합니다.

print("=== 나의 기본 프로필 ===")  # 프로필 시작을 알리는 제목을 출력합니다.
print(f"과정명: {course_name}")  # f-string을 사용해 course_name의 값을 문장 안에 넣습니다.
print(f"이름: {name}")  # name 변수의 값을 출력합니다.
print(f"나이: {age}세")  # 정수형 age 값을 문자열 문장 안에 넣어 출력합니다.
print(f"희망직무: {desired_job}")  # desired_job 변수의 값을 출력합니다.

print("\n=== 자료형 확인 ===")  # 줄을 바꾼 뒤 자료형 확인 구역을 시작합니다.
print("name 자료형:", type(name))  # name이 str 자료형 객체를 가리키는지 확인합니다.
print("age 자료형:", type(age))  # age가 int 자료형 객체를 가리키는지 확인합니다.
