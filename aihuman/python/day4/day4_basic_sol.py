# day4_basic_sol.py
# Basic 과제 풀이: 점수 1개의 합격 여부 판정

score = int(input("점수: "))  # 사용자에게 점수를 입력받고 정수로 변환합니다.

if score >= 60:  # 점수가 60점 이상인지 확인합니다.
    print("PASS")  # 조건이 True이면 PASS를 출력합니다.
else:  # 점수가 60점 미만인 경우를 처리합니다.
    print("RETRY")  # 조건이 False이면 RETRY를 출력합니다.
