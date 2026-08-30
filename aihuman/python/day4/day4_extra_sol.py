# day4_extra_sol.py
# AI휴먼 Day 4 추가 실습문제 풀이

def solution_01():
    name = input("이름: ")  # 이름을 입력받습니다.

    if name:  # 내용이 있는 문자열은 True처럼 평가됩니다.
        print("이름 입력 완료")  # 이름이 있으면 완료 메시지를 출력합니다.
    else:  # 빈 문자열은 False처럼 평가됩니다.
        print("이름 없음")  # 이름이 없음을 출력합니다.


def solution_02():
    grade = input("회원등급(NORMAL/GOLD/VIP): ").upper()  # 회원등급을 대문자로 변환합니다.

    if grade in ["NORMAL", "GOLD", "VIP"]:  # 허용된 값인지 검사합니다.
        print("정상 등급")  # 정상 등급을 출력합니다.
    else:  # 허용되지 않은 값입니다.
        print("입력 오류")  # 입력 오류를 출력합니다.

def solution_03():
    number = int(input("정수: "))  # 정수를 입력받습니다.

    if number % 2 == 0:  # 2로 나눈 나머지가 0인지 확인합니다.
        print("짝수")  # 짝수를 출력합니다.
    else:  # 나머지가 0이 아닌 경우입니다.
        print("홀수")  # 홀수를 출력합니다.


def solution_04():
    hour = int(input("시간(0~23): "))  # 시간을 입력받습니다.

    if hour < 0 or hour > 23:  # 유효한 시간 범위를 확인합니다.
        print("입력 오류")  # 입력 오류를 출력합니다.
    elif hour < 12:  # 12시 이전인지 확인합니다.
        print("AM")  # 오전을 출력합니다.
    else:  # 12~23시입니다.
        print("PM")  # 오후를 출력합니다.

def solution_05():
    month = int(input("월(1~12): "))  # 월을 입력받습니다.

    if month in [12, 1, 2]:  # 겨울 월인지 확인합니다.
        print("겨울")  # 겨울을 출력합니다.
    elif month in [3, 4, 5]:  # 봄 월인지 확인합니다.
        print("봄")  # 봄을 출력합니다.
    elif month in [6, 7, 8]:  # 여름 월인지 확인합니다.
        print("여름")  # 여름을 출력합니다.
    elif month in [9, 10, 11]:  # 가을 월인지 확인합니다.
        print("가을")  # 가을을 출력합니다.
    else:  # 1~12가 아닌 경우입니다.
        print("입력 오류")  # 입력 오류를 출력합니다.

def solution_6():
    price = int(input("구매금액: "))  # 구매금액을 입력받습니다.
    grade = input("회원등급(NORMAL/GOLD/VIP): ").upper()  # 회원등급을 대문자로 변환합니다.

    if grade not in ["NORMAL", "GOLD", "VIP"]:  # 회원등급을 검증합니다.
        print("입력 오류")  # 입력 오류를 출력합니다.
    elif price >= 50000 or grade in ["GOLD", "VIP"] and price >= 30000:  # 우수회원 조건입니다.
        print("무료배송")  # 무료배송을 출력합니다.
    else:  # 무료배송 조건을 만족하지 못한 경우입니다.
        print("배송비: 3,000원")  # 배송비를 출력합니다.

def solution_7():
    score = float(input("평균점수: "))  # 평균점수를 입력받습니다.
    attendance = float(input("출석률: "))  # 출석률을 입력받습니다.

    if score >= 95 and attendance >= 85:  # 우수 장학금 조건을 먼저 검사합니다.
        print("우수 장학금 대상")  # 우수 장학금 대상입니다.
    elif score >= 85 and attendance >= 90:  # 일반 장학금 조건입니다.
        print("장학금 대상")  # 장학금 대상입니다.
    else:  # 두 조건을 만족하지 못한 경우입니다.
        print("대상 아님")  # 대상이 아님을 출력합니다.

def solution_8():
    score = int(input("성과점수: "))  # 성과점수를 입력받습니다.
    late = int(input("지각횟수: "))  # 지각횟수를 입력받습니다.

    if score < 0 or score > 100 or late < 0:  # 입력값을 검증합니다.
        print("입력 오류")  # 입력 오류를 출력합니다.
    elif score >= 90 and late == 0:  # S등급 조건입니다.
        print("성과등급: S")  # S등급을 출력합니다.
    elif score >= 80 and late <= 2:  # A등급 조건입니다.
        print("성과등급: A")  # A등급을 출력합니다.
    elif score >= 70 and late <= 4:  # B등급 조건입니다.
        print("성과등급: B")  # B등급을 출력합니다.
    else:  # 나머지 경우입니다.
        print("성과등급: C")  # C등급을 출력합니다.

def solution_9():
    balance = int(input("현재 잔액: "))  # 현재 잔액을 입력받습니다.
    amount = int(input("출금금액: "))  # 출금금액을 입력받습니다.

    if amount <= 0:  # 출금금액이 올바른지 확인합니다.
        print("잘못된 금액")  # 잘못된 금액을 출력합니다.
    elif amount % 10000 != 0:  # 만원 단위인지 확인합니다.
        print("만원 단위로 입력")  # 만원 단위 입력을 안내합니다.
    elif amount > balance:  # 잔액보다 큰지 확인합니다.
        print("잔액 부족")  # 잔액 부족을 출력합니다.
    else:  # 정상 출금 조건입니다.
        balance = balance - amount  # 출금 후 잔액을 계산합니다.
        print(f"출금 후 잔액: {balance:,}원")  # 잔액을 출력합니다.

def solution_10():
    price = int(input("구매금액: "))  # 구매금액을 입력받습니다.
    grade = input("회원등급(NORMAL/GOLD/VIP): ").upper()  # 회원등급을 입력받습니다.
    coupon = input("쿠폰보유(Y/N): ").upper()  # 쿠폰 여부를 입력받습니다.

    if price < 0 or grade not in ["NORMAL", "GOLD", "VIP"] or coupon not in ["Y", "N"]:
        # 입력값의 유효성을 확인합니다.
        print("입력 오류")  # 입력 오류를 출력합니다.
    else:
        if price >= 100000 and grade == "VIP":  # 20% 할인 조건입니다.
            discount_rate = 0.20  # 할인율을 저장합니다.
        elif coupon == "Y" and price >= 50000:  # 15% 할인 조건입니다.
            discount_rate = 0.15  # 할인율을 저장합니다.
        elif grade in ["GOLD", "VIP"] and price >= 30000:  # 10% 할인 조건입니다.
            discount_rate = 0.10  # 할인율을 저장합니다.
        elif price >= 30000:  # 5% 할인 조건입니다.
            discount_rate = 0.05  # 할인율을 저장합니다.
        else:  # 할인 대상이 아닙니다.
            discount_rate = 0.0  # 할인율을 0으로 저장합니다.

        discount_price = int(price * discount_rate)  # 할인금액을 계산합니다.
        final_price = price - discount_price  # 최종 결제금액을 계산합니다.

        print(f"할인율: {discount_rate * 100:.0f}%")  # 할인율을 출력합니다.
        print(f"할인금액: {discount_price:,}원")  # 할인금액을 출력합니다.
        print(f"최종 결제금액: {final_price:,}원")  # 최종 결제금액을 출력합니다.
