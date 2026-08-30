# ============================================================
# AI휴먼 9일차 실습
# 주제: NumPy 배열의 구조와 기본 수치 연산
# ============================================================

# NumPy 라이브러리를 np라는 별칭으로 불러옵니다.
import numpy as np

# 화면에서 실습 구간을 구분하기 위한 함수를 정의합니다.
def print_section(title):
    # 구분선을 출력합니다.
    print("\n" + "=" * 60)
    # 현재 실습 제목을 출력합니다.
    print(title)
    # 구분선을 출력합니다.
    print("=" * 60)


# ------------------------------------------------------------
# 1. Python 리스트와 NumPy 배열 비교
# ------------------------------------------------------------
print_section("1. Python 리스트와 NumPy 배열 비교")

# Python 리스트에 네 개의 점수를 저장합니다.
python_scores = [70, 85, 90, 95]

# Python 리스트에 5를 더한 결과를 저장할 빈 리스트를 준비합니다.
python_result = []

# 리스트의 각 점수를 하나씩 반복합니다.
for score in python_scores:
    # 현재 점수에 5를 더한 값을 결과 리스트에 추가합니다.
    python_result.append(score + 5)

# Python 반복문으로 계산한 결과를 출력합니다.
print("Python 리스트 계산:", python_result)

# 같은 점수 데이터를 NumPy 배열로 생성합니다.
numpy_scores = np.array([70, 85, 90, 95])

# NumPy 배열 전체에 5를 한 번에 더하고 결과를 출력합니다.
print("NumPy 벡터 연산:", numpy_scores + 5)

# NumPy 배열 객체의 실제 자료형을 출력합니다.
print("배열 객체 타입:", type(numpy_scores))


# ------------------------------------------------------------
# 2. 여러 방식으로 배열 생성하기
# ------------------------------------------------------------
print_section("2. 여러 방식으로 배열 생성하기")

# 1차원 NumPy 배열을 생성합니다.
arr1 = np.array([10, 20, 30, 40, 50])

# 1차원 배열을 출력합니다.
print("np.array:", arr1)

# 0부터 10 미만까지 2씩 증가하는 배열을 생성합니다.
arr2 = np.arange(0, 10, 2)

# arange()로 만든 배열을 출력합니다.
print("np.arange:", arr2)

# 0부터 1까지를 5개의 동일한 간격으로 나눈 배열을 생성합니다.
arr3 = np.linspace(0, 1, 5)

# linspace()로 만든 배열을 출력합니다.
print("np.linspace:", arr3)

# 2행 3열을 모두 0으로 채운 배열을 생성합니다.
zeros = np.zeros((2, 3))

# 0으로 채운 배열을 출력합니다.
print("np.zeros:\n", zeros)

# 2행 3열을 모두 1로 채운 배열을 생성합니다.
ones = np.ones((2, 3))

# 1로 채운 배열을 출력합니다.
print("np.ones:\n", ones)

# 2행 2열을 숫자 7로 채운 배열을 생성합니다.
full = np.full((2, 2), 7)

# 지정값으로 채운 배열을 출력합니다.
print("np.full:\n", full)


# ------------------------------------------------------------
# 3. shape, ndim, size, dtype 확인하기
# ------------------------------------------------------------
print_section("3. shape, ndim, size, dtype 확인하기")

# 2행 3열의 정수 배열을 생성합니다.
student_scores = np.array([
    [80, 90, 85],
    [70, 75, 95]
])

# 배열 전체를 출력합니다.
print("학생 점수 배열:\n", student_scores)

# 배열의 각 축 크기를 튜플로 출력합니다.
print("shape:", student_scores.shape)

# 배열의 차원 수를 출력합니다.
print("ndim:", student_scores.ndim)

# 배열에 들어 있는 전체 원소 수를 출력합니다.
print("size:", student_scores.size)

# 배열 원소의 자료형을 출력합니다.
print("dtype:", student_scores.dtype)


# ------------------------------------------------------------
# 4. dtype 지정과 자료형 변환
# ------------------------------------------------------------
print_section("4. dtype 지정과 자료형 변환")

# 정수 데이터를 float64 자료형으로 지정하여 배열을 생성합니다.
float_scores = np.array([70, 85, 90], dtype=np.float64)

# 실수형 배열을 출력합니다.
print("float 배열:", float_scores)

# 실수형 배열의 dtype을 출력합니다.
print("float dtype:", float_scores.dtype)

# 실수형 배열을 int32 자료형으로 변환합니다.
int_scores = float_scores.astype(np.int32)

# 변환된 정수 배열을 출력합니다.
print("int 변환 배열:", int_scores)

# 변환된 배열의 dtype을 출력합니다.
print("int dtype:", int_scores.dtype)


# ------------------------------------------------------------
# 5. NumPy 주요 상수 확인
# ------------------------------------------------------------
print_section("5. NumPy 주요 상수 확인")

# 원주율 pi 값을 출력합니다.
print("np.pi:", np.pi)

# 자연상수 e 값을 출력합니다.
print("np.e:", np.e)

# 양의 무한대를 출력합니다.
print("np.inf:", np.inf)

# 결측값 표현에 자주 사용하는 NaN을 출력합니다.
print("np.nan:", np.nan)

# NaN 값끼리 직접 비교한 결과를 출력합니다.
print("np.nan == np.nan:", np.nan == np.nan)

# np.isnan()으로 NaN 여부를 올바르게 확인합니다.
print("np.isnan(np.nan):", np.isnan(np.nan))


# ------------------------------------------------------------
# 6. 1차원 배열 인덱싱과 슬라이싱
# ------------------------------------------------------------
print_section("6. 1차원 배열 인덱싱과 슬라이싱")

# 여섯 개의 값을 가진 1차원 배열을 생성합니다.
values = np.array([10, 20, 30, 40, 50, 60])

# 첫 번째 원소를 출력합니다.
print("첫 번째 값:", values[0])

# 마지막 원소를 출력합니다.
print("마지막 값:", values[-1])

# 인덱스 1부터 3까지의 값을 슬라이싱하여 출력합니다.
print("values[1:4]:", values[1:4])

# 처음부터 인덱스 2까지의 값을 출력합니다.
print("values[:3]:", values[:3])

# 처음부터 끝까지 두 칸씩 건너뛴 값을 출력합니다.
print("values[::2]:", values[::2])


# ------------------------------------------------------------
# 7. 2차원 배열 인덱싱과 슬라이싱
# ------------------------------------------------------------
print_section("7. 2차원 배열 인덱싱과 슬라이싱")

# 3행 4열의 2차원 배열을 생성합니다.
matrix = np.array([
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
])

# 전체 배열을 출력합니다.
print("전체 배열:\n", matrix)

# 2행 3열 위치의 값을 출력합니다.
print("matrix[1, 2]:", matrix[1, 2])

# 두 번째 행 전체를 출력합니다.
print("두 번째 행:", matrix[1])

# 세 번째 열 전체를 출력합니다.
print("세 번째 열:", matrix[:, 2])

# 첫 두 행과 두 번째~세 번째 열을 잘라 출력합니다.
print("부분 배열:\n", matrix[0:2, 1:3])


# ------------------------------------------------------------
# 8. 조건 인덱싱
# ------------------------------------------------------------
print_section("8. 조건 인덱싱")

# 분석할 점수 배열을 생성합니다.
exam_scores = np.array([55, 70, 82, 91, 68, 88, 76, 95])

# 80점 이상인지 비교한 Boolean 배열을 생성합니다.
condition = exam_scores >= 80

# Boolean 조건 배열을 출력합니다.
print("80점 이상 조건:", condition)

# 조건이 True인 점수만 추출하여 출력합니다.
print("80점 이상 점수:", exam_scores[condition])

# 70점 이상이면서 90점 미만인 점수만 추출합니다.
mid_scores = exam_scores[(exam_scores >= 70) & (exam_scores < 90)]

# 두 조건을 만족하는 점수를 출력합니다.
print("70점 이상 90점 미만:", mid_scores)

# np.where()로 90점 이상인 데이터의 인덱스를 찾습니다.
high_indices = np.where(exam_scores >= 90)[0]

# 90점 이상인 데이터의 인덱스를 출력합니다.
print("90점 이상 인덱스:", high_indices)


# ------------------------------------------------------------
# 9. 벡터 연산
# ------------------------------------------------------------
print_section("9. 벡터 연산")

# 연산 대상 배열을 생성합니다.
base = np.array([10, 20, 30, 40])

# 모든 원소에 5를 더한 결과를 출력합니다.
print("+ 5:", base + 5)

# 모든 원소에서 3을 뺀 결과를 출력합니다.
print("- 3:", base - 3)

# 모든 원소에 2를 곱한 결과를 출력합니다.
print("* 2:", base * 2)

# 모든 원소를 10으로 나눈 결과를 출력합니다.
print("/ 10:", base / 10)

# 모든 원소를 제곱한 결과를 출력합니다.
print("제곱:", base ** 2)

# 첫 번째 배열을 생성합니다.
a = np.array([1, 2, 3])

# 두 번째 배열을 생성합니다.
b = np.array([10, 20, 30])

# 같은 위치의 원소끼리 더한 결과를 출력합니다.
print("a + b:", a + b)

# 같은 위치의 원소끼리 곱한 결과를 출력합니다.
print("a * b:", a * b)


# ------------------------------------------------------------
# 10. 집계 함수와 axis
# ------------------------------------------------------------
print_section("10. 집계 함수와 axis")

# 학생 4명의 국어, 영어, 수학 점수를 2차원 배열로 생성합니다.
scores = np.array([
    [78, 85, 92],
    [88, 90, 76],
    [95, 82, 89],
    [67, 74, 80]
])

# 전체 점수의 합계를 출력합니다.
print("전체 합계:", scores.sum())

# 전체 점수의 평균을 출력합니다.
print("전체 평균:", scores.mean())

# 전체 점수의 최댓값을 출력합니다.
print("전체 최고점:", scores.max())

# 전체 점수의 최솟값을 출력합니다.
print("전체 최저점:", scores.min())

# 각 열, 즉 과목별 평균을 계산합니다.
subject_avg = scores.mean(axis=0)

# 과목별 평균을 출력합니다.
print("과목별 평균:", subject_avg)

# 각 행, 즉 학생별 평균을 계산합니다.
student_avg = scores.mean(axis=1)

# 학생별 평균을 출력합니다.
print("학생별 평균:", student_avg)

# 평균이 85점 이상인 학생의 인덱스를 찾습니다.
excellent_students = np.where(student_avg >= 85)[0]

# 우수 학생의 인덱스를 출력합니다.
print("평균 85점 이상 학생 인덱스:", excellent_students)


# ------------------------------------------------------------
# 11. reshape(), flatten(), 전치
# ------------------------------------------------------------
print_section("11. reshape(), flatten(), 전치")

# 1부터 12까지의 값을 가진 1차원 배열을 생성합니다.
sequence = np.arange(1, 13)

# 원래 1차원 배열을 출력합니다.
print("원본:", sequence)

# 12개의 원소를 3행 4열로 재구성합니다.
reshaped = sequence.reshape(3, 4)

# 재구성한 2차원 배열을 출력합니다.
print("3행 4열:\n", reshaped)

# 두 번째 축의 크기를 NumPy가 자동 계산하도록 -1을 사용합니다.
auto_reshape = sequence.reshape(2, -1)

# 자동 계산된 2행 6열 배열을 출력합니다.
print("2행 자동 열 계산:\n", auto_reshape)

# 2차원 배열을 1차원 복사본으로 펼칩니다.
flattened = reshaped.flatten()

# 펼친 배열을 출력합니다.
print("flatten 결과:", flattened)

# 행과 열을 뒤바꾼 전치 배열을 출력합니다.
print("전치 결과:\n", reshaped.T)


# ------------------------------------------------------------
# 12. 브로드캐스팅
# ------------------------------------------------------------
print_section("12. 브로드캐스팅")

# 두 학생의 세 과목 점수를 생성합니다.
raw_scores = np.array([
    [70, 80, 90],
    [75, 85, 95]
])

# 세 과목에 각각 적용할 보정 점수를 생성합니다.
bonus = np.array([2, 3, 1])

# 2차원 배열의 각 행에 1차원 bonus 배열을 더합니다.
adjusted_scores = raw_scores + bonus

# 원래 점수를 출력합니다.
print("원래 점수:\n", raw_scores)

# 과목별 보정 점수를 출력합니다.
print("보정 점수:", bonus)

# 브로드캐스팅된 계산 결과를 출력합니다.
print("보정 후 점수:\n", adjusted_scores)


# ------------------------------------------------------------
# 13. 종합 실습 - NumPy 성적 분석
# ------------------------------------------------------------
print_section("13. 종합 실습 - NumPy 성적 분석")

# 학생 이름을 NumPy 문자열 배열로 생성합니다.
students = np.array(["민준", "서연", "지훈", "하은", "도윤"])

# 학생별 국어, 영어, 수학 점수를 2차원 배열로 생성합니다.
final_scores = np.array([
    [82, 91, 88],
    [95, 87, 92],
    [76, 80, 79],
    [88, 94, 90],
    [69, 73, 81]
])

# 학생별 평균을 계산합니다.
final_student_avg = final_scores.mean(axis=1)

# 과목별 평균을 계산합니다.
final_subject_avg = final_scores.mean(axis=0)

# 전체 최고점을 계산합니다.
final_max = final_scores.max()

# 전체 최저점을 계산합니다.
final_min = final_scores.min()

# 학생별 평균을 소수점 둘째 자리까지 반올림하여 출력합니다.
print("학생별 평균:", np.round(final_student_avg, 2))

# 과목별 평균을 소수점 둘째 자리까지 반올림하여 출력합니다.
print("과목별 평균:", np.round(final_subject_avg, 2))

# 전체 최고점을 출력합니다.
print("전체 최고점:", final_max)

# 전체 최저점을 출력합니다.
print("전체 최저점:", final_min)

# 평균이 85점 이상인 학생만 선택하는 조건을 만듭니다.
selected_mask = final_student_avg >= 85

# 조건을 이용하여 학생 이름만 추출합니다.
selected_students = students[selected_mask]

# 조건을 이용하여 해당 학생의 평균만 추출합니다.
selected_avg = final_student_avg[selected_mask]

# 평균 85점 이상 학생의 이름을 출력합니다.
print("평균 85점 이상 학생:", selected_students)

# 평균 85점 이상 학생의 평균 점수를 출력합니다.
print("선발 학생 평균:", np.round(selected_avg, 2))

# 가장 높은 평균을 가진 학생의 위치를 찾습니다.
best_index = np.argmax(final_student_avg)

# 가장 높은 평균을 가진 학생의 이름과 평균을 출력합니다.
print(
    "최우수 학생:",
    students[best_index],
    "/ 평균:",
    round(float(final_student_avg[best_index]), 2)
)


# ------------------------------------------------------------
# 14. 핵심 확인
# ------------------------------------------------------------
print_section("14. 핵심 확인")

# 오늘 실습에서 확인해야 할 항목을 출력합니다.
print("1) ndarray 생성과 구조 확인")

# shape 관련 확인 항목을 출력합니다.
print("2) shape / ndim / size / dtype")

# 데이터 추출 관련 확인 항목을 출력합니다.
print("3) 인덱싱 / 슬라이싱 / 조건 인덱싱")

# 연산 관련 확인 항목을 출력합니다.
print("4) 벡터 연산 / 집계 / axis")

# 형태 변경 관련 확인 항목을 출력합니다.
print("5) reshape / flatten / transpose")

# 확장 연산 관련 확인 항목을 출력합니다.
print("6) 브로드캐스팅")
