# day3_basic_sol.py
# AI휴먼 Day 3 Basic 과제 풀이
# 주제: 기본 주문 금액 계산기

# 사용자에게 상품명을 문자열로 입력받습니다.
product = input("상품명: ")

# 상품 단가를 입력받고 계산을 위해 int로 변환합니다.
unit_price = int(input("상품 단가: "))

# 구매 수량을 입력받고 계산을 위해 int로 변환합니다.
quantity = int(input("구매 수량: "))

# 단가와 수량을 곱하여 주문금액을 계산합니다.
total = unit_price * quantity

# 구분선을 출력합니다.
print("=" * 35)

# 입력받은 상품명을 출력합니다.
print(f"상품명: {product}")

# 단가를 천 단위 쉼표와 함께 출력합니다.
print(f"단가: {unit_price:,}원")

# 구매 수량을 출력합니다.
print(f"수량: {quantity}개")

# 계산된 주문금액을 천 단위 쉼표와 함께 출력합니다.
print(f"주문금액: {total:,}원")

# 구분선을 출력합니다.
print("=" * 35)
