[AI휴먼 6일차 추가 실습 풀이]
주제: Python 함수 실습
문항 수: 10문항

============================================================
1. 리스트에서 최댓값과 최솟값 찾기
============================================================

def find_min_max(numbers):
    # 첫 번째 값을 최솟값과 최댓값의 초기값으로 지정합니다.
    min_value = numbers[0]
    max_value = numbers[0]

    # 리스트의 숫자를 하나씩 확인합니다.
    for number in numbers:
        # 현재 값이 더 작으면 최솟값을 변경합니다.
        if number < min_value:
            min_value = number

        # 현재 값이 더 크면 최댓값을 변경합니다.
        if number > max_value:
            max_value = number

    # 최솟값과 최댓값을 동시에 반환합니다.
    return min_value, max_value


numbers = [17, 5, 23, 9, 11]
result = find_min_max(numbers)
print(result)


============================================================
2. 합격자 점수만 추출하는 함수
============================================================

def get_pass_scores(scores):
    # 조건을 만족하는 점수를 저장할 리스트를 생성합니다.
    pass_scores = []

    # 모든 점수를 순서대로 확인합니다.
    for score in scores:
        # 60점 이상인 점수만 저장합니다.
        if score >= 60:
            pass_scores.append(score)

    # 완성된 리스트를 반환합니다.
    return pass_scores


scores = [45, 72, 88, 59, 60, 91]
print(get_pass_scores(scores))


============================================================
3. 문자열 분석 결과 반환 함수
============================================================

def analyze_text(text):
    # 전체 문자 수를 계산합니다.
    total_count = len(text)

    # 공백을 제외한 문자 수를 저장합니다.
    non_space_count = 0

    # 숫자 문자의 개수를 저장합니다.
    digit_count = 0

    # 문자열의 문자를 하나씩 확인합니다.
    for char in text:
        # 공백이 아니면 개수를 증가시킵니다.
        if char != " ":
            non_space_count += 1

        # 숫자 문자이면 숫자 개수를 증가시킵니다.
        if char.isdigit():
            digit_count += 1

    # 여러 결과를 하나의 딕셔너리로 반환합니다.
    return {
        "전체문자수": total_count,
        "공백제외문자수": non_space_count,
        "숫자개수": digit_count
    }


text = "Python 3 Function 2026"
print(analyze_text(text))


============================================================
4. 학생별 총점과 평균 계산 함수
============================================================

students = {
    "김철수": [80, 90, 70],
    "이영희": [95, 88, 92],
    "박민수": [60, 75, 68]
}


def calculate_student(name, scores):
    # 총점을 저장할 변수를 0으로 초기화합니다.
    total = 0

    # 점수를 하나씩 누적합니다.
    for score in scores:
        total += score

    # 총점을 과목 수로 나누어 평균을 계산합니다.
    average = total / len(scores)

    # 학생별 결과를 딕셔너리로 반환합니다.
    return {
        "이름": name,
        "총점": total,
        "평균": average
    }


# 모든 학생을 순회합니다.
for name, scores in students.items():
    # 학생별 결과를 함수로 계산합니다.
    result = calculate_student(name, scores)

    # 계산 결과를 출력합니다.
    print(result)


============================================================
5. 가변 인수를 이용한 합계 함수
============================================================

def sum_all(*args):
    # 전달된 모든 값의 합계를 저장합니다.
    total = 0

    # args는 전달된 인수들이 저장된 튜플입니다.
    for number in args:
        total += number

    # 계산한 합계를 반환합니다.
    return total


print(sum_all(10, 20, 30))
print(sum_all(1, 2, 3, 4, 5))


============================================================
6. 기본값 매개변수를 이용한 급여 계산 함수
============================================================

def calculate_salary(base_salary, bonus_rate=0.1):
    # 기본 급여에 보너스를 더한 최종 급여를 계산합니다.
    final_salary = base_salary + (base_salary * bonus_rate)

    # 최종 급여를 반환합니다.
    return final_salary


# 보너스율을 생략하면 기본값 0.1이 적용됩니다.
print(calculate_salary(3000000))

# 보너스율을 직접 전달하면 전달한 값이 적용됩니다.
print(calculate_salary(3000000, 0.2))


============================================================
7. 함수를 이용한 학생 성적 처리
============================================================

students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 76,
    "최지우": 64
}


def get_grade(score):
    # 점수에 따라 등급을 반환합니다.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def make_report(students):
    # 각 학생의 결과 문자열을 저장할 리스트입니다.
    report = []

    # 이름과 점수를 동시에 가져옵니다.
    for name, score in students.items():
        # 별도의 함수로 등급을 계산합니다.
        grade = get_grade(score)

        # 출력 형식에 맞는 문자열을 생성합니다.
        line = f"{name} : {score}점 / {grade}"

        # 완성된 한 줄을 리스트에 추가합니다.
        report.append(line)

    # 전체 보고서 리스트를 반환합니다.
    return report


result = make_report(students)

for line in result:
    print(line)


============================================================
8. 고차함수 - 계산 함수를 인수로 전달하기
============================================================

def add(a, b):
    # 두 수의 합을 반환합니다.
    return a + b


def subtract(a, b):
    # 두 수의 차를 반환합니다.
    return a - b


def multiply(a, b):
    # 두 수의 곱을 반환합니다.
    return a * b


def calculate(a, b, operation):
    # operation에는 add, subtract, multiply와 같은 함수가 전달됩니다.
    result = operation(a, b)

    # 전달받은 함수의 실행 결과를 반환합니다.
    return result


print(calculate(10, 5, add))
print(calculate(10, 5, subtract))
print(calculate(10, 5, multiply))


# 핵심:
# calculate()는 다른 함수를 인수로 전달받으므로 고차함수입니다.
# add()처럼 괄호를 붙이면 함수가 즉시 실행되고,
# add처럼 괄호를 생략하면 함수 객체 자체를 전달합니다.


============================================================
9. 콜백함수 - 주문 처리 완료 후 함수 호출하기
============================================================

def payment_complete(order_name):
    # 주문 처리 후 실행할 첫 번째 콜백함수입니다.
    print(f"[{order_name}] 결제가 완료되었습니다.")


def send_message(order_name):
    # 주문 처리 후 실행할 두 번째 콜백함수입니다.
    print(f"[{order_name}] 주문 완료 메시지를 전송했습니다.")


def process_order(order_name, callback):
    # 주문 처리 시작을 출력합니다.
    print(f"[{order_name}] 주문을 처리합니다.")

    # 주문 처리가 끝난 후 전달받은 함수를 호출합니다.
    callback(order_name)


process_order("노트북", payment_complete)
process_order("키보드", send_message)


# 핵심:
# callback 매개변수에는 실행할 함수 자체가 전달됩니다.
# process_order() 내부에서 특정 작업이 끝난 뒤 callback()을 실행합니다.
# 따라서 payment_complete와 send_message는 콜백함수 역할을 합니다.
# process_order()는 함수를 인수로 받기 때문에 고차함수이기도 합니다.


============================================================
10. 고차함수 + 콜백함수 - 점수 데이터 처리 시스템
============================================================

scores = [55, 72, 88, 91, 67, 100, 83]


def is_pass(score):
    # 60점 이상이면 True를 반환합니다.
    return score >= 60


def is_excellent(score):
    # 90점 이상이면 True를 반환합니다.
    return score >= 90


def filter_scores(scores, condition):
    # 조건을 만족하는 점수를 저장할 리스트입니다.
    result = []

    # 모든 점수를 하나씩 검사합니다.
    for score in scores:
        # 전달받은 조건 함수를 호출합니다.
        if condition(score):
            # 조건이 True이면 결과 리스트에 추가합니다.
            result.append(score)

    # 필터링된 점수 리스트를 반환합니다.
    return result


def print_result(title, result):
    # 전달받은 제목과 결과를 출력합니다.
    print(f"{title} : {result}")


def process_scores(scores, condition, callback, title="결과"):
    # condition 함수를 이용해 데이터를 필터링합니다.
    filtered_scores = filter_scores(scores, condition)

    # 처리가 끝난 후 callback 함수를 실행합니다.
    callback(title, filtered_scores)

    # 외부에서도 사용할 수 있도록 결과를 반환합니다.
    return filtered_scores


process_scores(
    scores,
    is_pass,
    print_result,
    "합격자 점수"
)

process_scores(
    scores,
    is_excellent,
    print_result,
    "우수자 점수"
)


# 핵심 구조:
#
# process_scores()
#   -> filter_scores(scores, condition)
#       -> condition(score)
#   -> callback(title, filtered_scores)
#
# condition은 "어떤 기준으로 처리할지"를 결정하는 함수이고,
# callback은 "처리가 끝난 후 무엇을 할지"를 결정하는 함수입니다.
# 따라서 고차함수와 콜백함수의 구조를 함께 연습할 수 있습니다.
