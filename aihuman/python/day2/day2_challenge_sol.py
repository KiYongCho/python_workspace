# day2_challenge_sol.py
# AI휴먼 과정 Day 2 Challenge 과제 풀이입니다.
# 목표: 외부 입력을 가정한 문자열 데이터의 자료형을 확인하고 올바르게 변환합니다.
# 참고: 형변환(Type Casting)은 Day 3에서 본격 학습합니다.

raw_age = "25"  # 외부에서 받은 나이 데이터는 문자열(str)이라고 가정합니다.
raw_score = "91.5"  # 외부에서 받은 점수 데이터도 문자열(str)이라고 가정합니다.
name = "홍길동"  # 사용자 이름을 문자열로 저장합니다.

print("=== 원본 데이터 자료형 확인 ===")  # 형변환 전에 원본 자료형을 먼저 확인합니다.
print("raw_age:", raw_age, type(raw_age))  # raw_age 값과 자료형 str을 함께 출력합니다.
print("raw_score:", raw_score, type(raw_score))  # raw_score 값과 자료형 str을 함께 출력합니다.
print("name:", name, type(name))  # name 값과 자료형 str을 함께 출력합니다.

# 잘못된 사례 A: age = float(raw_age)  # 나이를 정수로 관리하려는 요구사항과 맞지 않는 형변환입니다.
age = int(raw_age)  # 문자열 "25"를 정수 25로 변환하여 나이를 int로 관리합니다.

# 잘못된 사례 B: score = int(raw_score)  # int("91.5")는 소수점 문자열을 바로 정수로 바꿀 수 없어 오류가 납니다.
score = float(raw_score)  # 문자열 "91.5"를 실수 91.5로 변환하여 소수점 점수를 유지합니다.

print("\n=== 수정 후 데이터 ===")  # 올바르게 형변환한 결과를 확인하는 구역입니다.
print("age:", age, type(age))  # age가 정수값 25와 int 자료형을 갖는지 확인합니다.
print("score:", score, type(score))  # score가 실수값 91.5와 float 자료형을 갖는지 확인합니다.

print("\n=== 최종 문장 ===")  # 요구사항의 최종 문장을 출력할 준비를 합니다.
print(f"{name}님의 나이는 {age}세이고 사전점수는 {score}점입니다.")  # f-string으로 여러 변수를 한 문장에 삽입합니다.

# 질문 1 답: "25"는 따옴표로 감싼 문자열(str)이고, 25는 계산에 사용할 수 있는 정수(int)입니다.
# 질문 2 답: type()을 먼저 확인하면 예상한 자료형과 실제 자료형이 같은지 확인하여 오류 원인을 더 빨리 찾을 수 있습니다.

portfolio_url = None  # 아직 포트폴리오 URL이 없다는 의미로 None 값을 저장합니다.
print("\nportfolio_url:", portfolio_url, type(portfolio_url))  # None 값과 NoneType 자료형을 함께 확인합니다.
