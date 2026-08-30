# day5_basic_sol.py
# AI휴먼 과정 5일차 Basic 과제 풀이

# 처리할 점수 5개를 리스트에 저장합니다.
scores = [72, 88, 95, 61, 83]

# 리스트의 점수를 하나씩 score 변수에 저장하며 반복합니다.
for score in scores:
    # 현재 점수가 80점 이상인지 확인합니다.
    if score >= 80:
        # 조건이 참이면 PASS를 result에 저장합니다.
        result = "PASS"
    # 80점 미만인 경우를 처리합니다.
    else:
        # 조건이 거짓이면 RETRY를 result에 저장합니다.
        result = "RETRY"

    # 현재 점수와 판정 결과를 출력합니다.
    print(f"{score}점 : {result}")
