# Day 10 Basic 과제 풀이: 직원 교육 참석 데이터 점검

# pandas 라이브러리를 pd라는 별칭으로 불러옵니다.
import pandas as pd


# 직원 교육 데이터를 딕셔너리로 준비합니다.
training_data = {
    # 사번 데이터를 저장합니다.
    "사번": ["E101", "E102", "E103", "E104", "E105", "E106"],
    # 이름 데이터를 저장합니다.
    "이름": ["김지훈", "이수빈", "박현우", "정예린", "최민석", "한서진"],
    # 부서 데이터를 저장합니다.
    "부서": ["개발", "기획", "영업", "개발", "기획", "영업"],
    # 교육점수 데이터를 저장합니다.
    "교육점수": [88, 92, 76, 95, 84, 81],
    # 교육시간 데이터를 저장합니다.
    "교육시간": [8, 10, 6, 12, 8, 7],
}

# 딕셔너리를 DataFrame으로 변환합니다.
source_df = pd.DataFrame(training_data)

# DataFrame을 CSV 파일로 저장합니다.
source_df.to_csv("employee_training.csv", index=False, encoding="utf-8-sig")

# 저장한 CSV 파일을 다시 읽어 DataFrame으로 만듭니다.
employee_df = pd.read_csv("employee_training.csv", encoding="utf-8-sig")

# 첫 번째 출력 구간의 제목을 출력합니다.
print("=== 1. 데이터 미리보기 ===")

# 처음 3개 행을 출력합니다.
print("[처음 3개 행]")
print(employee_df.head(3))

# 마지막 2개 행을 출력합니다.
print("\n[마지막 2개 행]")
print(employee_df.tail(2))

# 두 번째 출력 구간의 제목을 출력합니다.
print("\n=== 2. 데이터 크기와 컬럼 ===")

# DataFrame의 행 수를 출력합니다.
print("행 수:", employee_df.shape[0])

# DataFrame의 열 수를 출력합니다.
print("열 수:", employee_df.shape[1])

# 컬럼 이름을 리스트로 변환해 출력합니다.
print("컬럼:", list(employee_df.columns))

# 세 번째 출력 구간의 제목을 출력합니다.
print("\n=== 3. 컬럼별 dtype ===")

# 각 컬럼의 dtype을 출력합니다.
print(employee_df.dtypes)

# 네 번째 출력 구간의 제목을 출력합니다.
print("\n=== 4. info() 결과 ===")

# info()를 이용해 구조와 Non-Null Count를 출력합니다.
employee_df.info()

# 교육점수 Series를 선택합니다.
score = employee_df["교육점수"]

# 다섯 번째 출력 구간의 제목을 출력합니다.
print("\n=== 5. 교육점수 기초통계 ===")

# 교육점수 평균을 소수 둘째 자리까지 출력합니다.
print(f"평균: {score.mean():.2f}")

# 교육점수 최솟값을 출력합니다.
print("최솟값:", score.min())

# 교육점수 최댓값을 출력합니다.
print("최댓값:", score.max())

# 여섯 번째 출력 구간의 제목을 출력합니다.
print("\n=== 6. 부서별 직원 수 ===")

# 부서별 데이터 개수를 출력합니다.
print(employee_df["부서"].value_counts())
