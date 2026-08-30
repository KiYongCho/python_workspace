# day6_basic_sol.py
# AI휴먼 day6 Basic 과제 풀이

# 두 수를 전달받아 합계를 반환하는 함수를 정의합니다.
def add_numbers(a, b):
    # a와 b를 더한 값을 result 변수에 저장합니다.
    result = a + b
    # 계산한 합계를 함수 호출 위치로 반환합니다.
    return result

# 10과 20을 전달한 결과를 출력합니다.
print(add_numbers(10, 20))

# 3과 7을 전달한 결과를 출력합니다.
print(add_numbers(3, 7))

# -5와 8을 전달한 결과를 출력합니다.
print(add_numbers(-5, 8))
