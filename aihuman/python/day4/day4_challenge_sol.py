# day4_challenge_sol.py
# Challenge 과제 풀이: 점수 + 출석률 기반 최종 합격 판정기

score = int(input("점수: "))  # 점수를 입력받아 정수로 변환합니다.
attendance = int(input("출석률: "))  # 출석률을 입력받아 정수로 변환합니다.

if score < 0 or score > 100 or attendance < 0 or attendance > 100:  # 두 입력 중 하나라도 정상 범위를 벗어났는지 확인합니다.
    print("입력 오류")  # 잘못된 입력이 있으면 판정을 중단하고 오류를 출력합니다.
elif score >= 90 and attendance >= 95:  # 우수 합격 기준을 먼저 확인합니다.
    print("최종 판정: 우수 합격")  # 두 우수 기준을 모두 만족하면 우수 합격을 출력합니다.
elif score >= 70 and attendance >= 80:  # 일반 합격 기준을 확인합니다.
    print("최종 판정: 합격")  # 점수와 출석률 기준을 모두 만족하면 합격을 출력합니다.
elif attendance < 80:  # 합격하지 못한 경우 중 출석률이 80 미만인지 확인합니다.
    print("최종 판정: 불합격 - 출석률 미달")  # 출석률 부족 사유를 출력합니다.
else:  # 출석률은 기준을 만족하지만 점수가 70 미만인 경우입니다.
    print("최종 판정: 불합격 - 점수 미달")  # 점수 부족 사유를 출력합니다.
