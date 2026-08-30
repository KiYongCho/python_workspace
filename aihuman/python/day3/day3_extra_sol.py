# ============================================================
# AI휴먼 day3 Extra 실무형 실습과제 풀이
# 과제명: 기업교육 견적·손익 계산기
# 학습범위: day1 ~ day3
# ============================================================

# 프로그램의 시작을 보기 쉽도록 구분선을 출력합니다.
print("=" * 60)

# 프로그램 제목을 출력합니다.
print("기업교육 견적·손익 계산기")

# 다시 구분선을 출력합니다.
print("=" * 60)

# 회사명을 문자열로 입력받습니다.
company_name = input("회사명: ")

# 교육과정명을 문자열로 입력받습니다.
course_name = input("교육과정명: ")

# 참가 인원은 계산에 사용해야 하므로 int()로 정수 변환합니다.
participants = int(input("참가 인원(명): "))

# 총 교육시간은 7.5시간처럼 소수 입력도 가능하도록 float()로 변환합니다.
total_hours = float(input("총 교육시간(시간): "))

# 고객에게 청구할 시간당 교육비를 정수로 입력받습니다.
sales_hourly_rate = int(input("고객 청구 시간당 교육비(원): "))

# 강사에게 지급할 시간당 강사료를 정수로 입력받습니다.
instructor_hourly_pay = int(input("강사 지급 시간당 강사료(원): "))

# 참가자 1명당 필요한 교재 및 실습비를 정수로 입력받습니다.
material_unit_cost = int(input("1인당 교재/실습비(원): "))

# 장소 대관비와 장비 사용비를 합한 비용을 정수로 입력받습니다.
venue_equipment_cost = int(input("장소 및 장비 비용(원): "))

# 할인율은 7.5%처럼 소수 입력이 가능하도록 float()로 변환합니다.
discount_rate = float(input("고객 할인율(%): "))

# 출력 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 최소 권장 참가 인원을 변수에 저장합니다.
MIN_PARTICIPANTS = 5

# 최대 권장 참가 인원을 변수에 저장합니다.
MAX_PARTICIPANTS = 30

# 회사가 목표로 하는 최소 이익률을 저장합니다.
TARGET_MARGIN_RATE = 25.0

# 총 교육시간과 고객 청구 시간당 교육비를 곱해 교육 판매금액을 계산합니다.
training_sales = total_hours * sales_hourly_rate

# 참가 인원과 1인당 교재/실습비를 곱해 전체 교재/실습비를 계산합니다.
material_cost = participants * material_unit_cost

# 교육 판매금액, 교재/실습비, 장소/장비비를 더해 할인 전 견적금액을 계산합니다.
subtotal = training_sales + material_cost + venue_equipment_cost

# 할인 전 견적금액에 할인율을 적용해 실제 할인금액을 계산합니다.
discount_amount = subtotal * discount_rate / 100

# 할인 전 견적금액에서 할인금액을 빼 최종 계약 예상금액을 계산합니다.
final_contract_amount = subtotal - discount_amount

# 총 교육시간과 강사 지급 시간당 강사료를 곱해 전체 강사비를 계산합니다.
instructor_cost = total_hours * instructor_hourly_pay

# 강사비, 전체 교재/실습비, 장소/장비비를 더해 전체 원가를 계산합니다.
total_cost = instructor_cost + material_cost + venue_equipment_cost

# 최종 계약 예상금액에서 전체 원가를 빼 예상 이익을 계산합니다.
expected_profit = final_contract_amount - total_cost

# 예상 이익을 최종 계약 예상금액으로 나눈 뒤 100을 곱해 예상 이익률을 계산합니다.
profit_margin_rate = expected_profit / final_contract_amount * 100

# 예상 이익이 0보다 큰지 비교하여 True 또는 False를 저장합니다.
is_profitable = expected_profit > 0

# 참가 인원이 최소 인원 이상인지 비교합니다.
is_min_participant_ok = participants >= MIN_PARTICIPANTS

# 참가 인원이 최대 인원 이하인지 비교합니다.
is_max_participant_ok = participants <= MAX_PARTICIPANTS

# 두 비교 결과를 and로 연결해 권장 참가 인원 범위 충족 여부를 계산합니다.
is_participant_range_ok = is_min_participant_ok and is_max_participant_ok

# 예상 이익률이 목표 이익률 이상인지 비교하여 True 또는 False를 저장합니다.
is_target_margin_ok = profit_margin_rate >= TARGET_MARGIN_RATE

# 세 가지 사업성 조건을 모두 and로 연결해 최종 사업 진행 기준을 계산합니다.
can_proceed = is_profitable and is_participant_range_ok and is_target_margin_ok

# 견적서 시작을 알리는 구분선을 출력합니다.
print("-" * 60)

# 리포트 제목을 출력합니다.
print("기업교육 견적 및 손익 리포트")

# 다시 구분선을 출력합니다.
print("-" * 60)

# 입력받은 회사명을 출력합니다.
print(f"회사명             : {company_name}")

# 입력받은 교육과정명을 출력합니다.
print(f"교육과정           : {course_name}")

# 참가 인원을 정수 그대로 출력합니다.
print(f"참가 인원          : {participants}명")

# 총 교육시간을 소수점 첫째 자리까지 출력합니다.
print(f"총 교육시간        : {total_hours:.1f}시간")

# 견적 부분과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 견적 영역의 제목을 출력합니다.
print("[견적]")

# 교육 판매금액에 천 단위 콤마를 적용해 출력합니다.
print(f"교육 판매금액      : {training_sales:,.0f}원")

# 전체 교재/실습비에 천 단위 콤마를 적용해 출력합니다.
print(f"교재/실습비        : {material_cost:,}원")

# 장소 및 장비 비용에 천 단위 콤마를 적용해 출력합니다.
print(f"장소/장비비        : {venue_equipment_cost:,}원")

# 할인 전 견적금액에 천 단위 콤마를 적용해 출력합니다.
print(f"할인 전 견적금액   : {subtotal:,.0f}원")

# 할인율을 소수점 첫째 자리까지 출력합니다.
print(f"할인율             : {discount_rate:.1f}%")

# 할인금액에 천 단위 콤마를 적용해 출력합니다.
print(f"할인금액           : {discount_amount:,.0f}원")

# 최종 계약 예상금액에 천 단위 콤마를 적용해 출력합니다.
print(f"최종 계약 예상금액 : {final_contract_amount:,.0f}원")

# 손익 영역과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 손익 영역의 제목을 출력합니다.
print("[예상 원가 및 손익]")

# 강사비에 천 단위 콤마를 적용해 출력합니다.
print(f"강사비             : {instructor_cost:,.0f}원")

# 총 원가에 천 단위 콤마를 적용해 출력합니다.
print(f"총 원가            : {total_cost:,.0f}원")

# 예상 이익에 천 단위 콤마를 적용해 출력합니다.
print(f"예상 이익          : {expected_profit:,.0f}원")

# 예상 이익률을 소수점 둘째 자리까지 출력합니다.
print(f"예상 이익률        : {profit_margin_rate:.2f}%")

# 사업성 점검 영역과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 사업성 점검 영역의 제목을 출력합니다.
print("[사업성 점검]")

# 이익 발생 여부를 Boolean 값으로 출력합니다.
print(f"이익 발생 여부         : {is_profitable}")

# 권장 참가 인원 범위를 만족하는지 Boolean 값으로 출력합니다.
print(f"권장 인원 충족 여부    : {is_participant_range_ok}")

# 목표 이익률을 만족하는지 Boolean 값으로 출력합니다.
print(f"목표 이익률 충족 여부  : {is_target_margin_ok}")

# 전체 사업 진행 기준을 만족하는지 Boolean 값으로 출력합니다.
print(f"사업 진행 기준 충족    : {can_proceed}")

# 자료형 확인 영역과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 자료형 확인 영역의 제목을 출력합니다.
print("[자료형 확인]")

# 회사명 변수의 자료형이 str인지 확인합니다.
print(f"company_name 자료형 : {type(company_name)}")

# 참가 인원 변수의 자료형이 int인지 확인합니다.
print(f"participants 자료형 : {type(participants)}")

# 총 교육시간 변수의 자료형이 float인지 확인합니다.
print(f"total_hours 자료형  : {type(total_hours)}")

# 사업 진행 기준 변수의 자료형이 bool인지 확인합니다.
print(f"can_proceed 자료형  : {type(can_proceed)}")

# 프로그램의 마지막 구분선을 출력합니다.
print("-" * 60)

# 프로그램 종료 메시지를 출력합니다.
print("견적 및 손익 계산이 완료되었습니다.")

# 마지막 구분선을 출력합니다.
print("-" * 60)
