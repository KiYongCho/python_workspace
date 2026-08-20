# day2_application_sol.py
# AI휴먼 과정 Day 2 Application 과제 풀이입니다.
# 목표: 여러 자료형과 재대입을 활용해 취업준비생 학습 프로필 카드를 만듭니다.

learner_name = "김AI"  # 학습자 이름을 str 자료형으로 저장합니다.
age = 24  # 나이를 int 자료형으로 저장합니다.
target_job = "데이터 분석가"  # 희망직무를 str 자료형으로 저장합니다.
python_experience_years = 0.5  # Python 경험기간을 소수점이 있는 float 자료형으로 저장합니다.
is_job_seeker = True  # 취업준비 여부를 참/거짓을 표현하는 bool 자료형으로 저장합니다.
portfolio_url = None  # 아직 포트폴리오가 없다는 의미로 None 값을 저장합니다.

print("=== AI휴먼 학습 프로필 카드 ===")  # 프로필 카드의 제목을 출력합니다.
print(f"이름: {learner_name}")  # 학습자 이름을 출력합니다.
print(f"나이: {age}세")  # 나이 정수값을 출력합니다.
print(f"희망직무: {target_job}")  # 희망직무를 출력합니다.
print(f"Python 경험: {python_experience_years}년")  # Python 경험기간을 출력합니다.
print(f"취업준비 여부: {is_job_seeker}")  # bool 형태의 취업준비 여부를 출력합니다.
print(f"포트폴리오: {portfolio_url}")  # None 값인 포트폴리오 주소를 출력합니다.

print("\n=== 자료형 점검 ===")  # 각 변수의 자료형을 확인하기 위한 제목을 출력합니다.
print("learner_name ->", type(learner_name))  # learner_name의 자료형이 str인지 확인합니다.
print("age ->", type(age))  # age의 자료형이 int인지 확인합니다.
print("target_job ->", type(target_job))  # target_job의 자료형이 str인지 확인합니다.
print("python_experience_years ->", type(python_experience_years))  # 경험기간의 자료형이 float인지 확인합니다.
print("is_job_seeker ->", type(is_job_seeker))  # 취업준비 여부의 자료형이 bool인지 확인합니다.
print("portfolio_url ->", type(portfolio_url))  # None 값의 자료형이 NoneType인지 확인합니다.

status = "학습 시작"  # status 변수에 첫 번째 상태 문자열을 저장합니다.
print("\n=== 상태 변경 ===")  # 상태 변경 구역의 제목을 출력합니다.
print("변경 전:", status)  # 재대입 전의 status 값을 출력합니다.

status = "Day 2 완료"  # 같은 status 변수에 새로운 문자열 값을 다시 대입합니다.
print("변경 후:", status)  # 재대입 후 변경된 status 값을 출력합니다.
