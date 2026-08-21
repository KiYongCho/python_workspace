# day3_application_sol.py
# AI휴먼 Day 3 Application 과제 풀이
# 주제: 할인율을 적용한 결제금액 계산기

# 상품명을 입력받습니다.
product = input("상품명: ")

# 단가를 입력받아 정수로 변환합니다.
unit_price = int(input("단가: "))

# 수량을 입력받아 정수로 변환합니다.
quantity = int(input("수량: "))

# 할인율은 소수값이 들어올 수 있으므로 float로 변환합니다.
discount_rate = float(input("할인율(%): "))

# 할인 전 주문금액을 계산합니다.
subtotal = unit_price * quantity

# 할인율은 백분율이므로 100으로 나누어 실제 비율로 사용합니다.
discount_amount = subtotal * discount_rate / 100

# 주문금액에서 할인금액을 빼 최종 결제금액을 계산합니다.
final_amount = subtotal - discount_amount

# 결과 영역의 시작을 표시합니다.
print("=" * 40)

# 상품명을 출력합니다.
print(f"상품명: {product}")

# 주문금액을 소수점 없이 천 단위 쉼표로 출력합니다.
print(f"주문금액: {subtotal:,.0f}원")

# 할인율을 소수점 한 자리까지 출력합니다.
print(f"할인율: {discount_rate:.1f}%")

# 할인금액을 소수점 없이 천 단위 쉼표로 출력합니다.
print(f"할인금액: {discount_amount:,.0f}원")

# 최종 결제금액을 소수점 없이 천 단위 쉼표로 출력합니다.
print(f"최종 결제금액: {final_amount:,.0f}원")

# 결과 영역의 끝을 표시합니다.
print("=" * 40)
