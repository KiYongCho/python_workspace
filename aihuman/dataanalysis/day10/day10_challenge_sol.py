# Day 10 Challenge 과제 풀이: 채용 지원자 데이터 사전 만들기

# pandas 라이브러리를 pd라는 별칭으로 불러옵니다.
import pandas as pd


# 채용 지원자 데이터를 딕셔너리로 준비합니다.
applicant_data = {
    # 지원자 식별 코드를 저장합니다.
    "지원ID": ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010"],
    # 지원 직무를 저장합니다.
    "지원직무": ["백엔드", "데이터분석", "프론트엔드", "AI엔지니어", "백엔드", "데이터분석", "AI엔지니어", "프론트엔드", "백엔드", "데이터분석"],
    # 전공을 저장합니다.
    "전공": ["컴퓨터공학", "통계학", "디자인", "전자공학", "경영학", "수학", "컴퓨터공학", "컴퓨터공학", "전자공학", "경영학"],
    # 경력년수를 저장합니다.
    "경력년수": [1, 0, 2, 1, 3, 1, 2, 0, 1, 2],
    # 코딩테스트 점수를 저장합니다.
    "코딩테스트": [82, 91, 78, 94, 75, 89, 96, 84, 87, 81],
    # 영어점수를 저장합니다.
    "영어점수": [845, 910, 800, 880, 920, 870, 935, 825, 860, 905],
}

# 딕셔너리를 DataFrame으로 변환합니다.
source_df = pd.DataFrame(applicant_data)

# 원본 지원자 데이터를 CSV 파일로 저장합니다.
source_df.to_csv("applicants.csv", index=False, encoding="utf-8-sig")

# 저장한 CSV 파일을 다시 읽어 applicants_df를 만듭니다.
applicants_df = pd.read_csv("applicants.csv", encoding="utf-8-sig")

# 데이터 미리보기 제목을 출력합니다.
print("=== 1. 데이터 미리보기 ===")

# 처음 5개 행을 출력합니다.
print("[head]")
print(applicants_df.head())

# 마지막 5개 행을 출력합니다.
print("\n[tail]")
print(applicants_df.tail())

# 데이터 구조 제목을 출력합니다.
print("\n=== 2. 데이터 구조 ===")

# 행과 열 수를 출력합니다.
print("shape:", applicants_df.shape)

# 컬럼 이름을 출력합니다.
print("columns:", list(applicants_df.columns))

# 각 컬럼의 dtype을 출력합니다.
print("\ndtypes")
print(applicants_df.dtypes)

# info()로 컬럼명, Non-Null Count, dtype 등을 출력합니다.
print("\n[info]")
applicants_df.info()

# 코딩테스트와 영어점수만 선택한 DataFrame을 만듭니다.
score_df = applicants_df[["코딩테스트", "영어점수"]]

# 선택한 점수 DataFrame을 출력합니다.
print("\n=== 3. 평가 점수 컬럼 ===")
print(score_df)

# 숫자형 컬럼의 기초통계를 출력합니다.
print("\n=== 4. 숫자형 기초통계 ===")
print(applicants_df.describe())

# 지원직무별 지원자 수를 출력합니다.
print("\n=== 5. 지원직무별 지원자 수 ===")
print(applicants_df["지원직무"].value_counts())

# 전공의 고유값 목록을 출력합니다.
print("\n=== 6. 전공 구성 ===")
print("고유값:", applicants_df["전공"].unique())

# 전공의 고유값 개수를 출력합니다.
print("고유값 개수:", applicants_df["전공"].nunique())

# 데이터 사전의 각 행을 저장할 빈 리스트를 생성합니다.
dictionary_rows = []

# 모든 컬럼명을 순서대로 반복합니다.
for column in applicants_df.columns:
    # 현재 컬럼을 Series로 선택합니다.
    series = applicants_df[column]

    # 현재 컬럼의 정보를 딕셔너리로 만들고 리스트에 추가합니다.
    dictionary_rows.append(
        {
            "컬럼명": column,
            "dtype": str(series.dtype),
            "전체행수": len(series),
            "Non-Null개수": series.count(),
            "고유값수": series.nunique(),
            "첫번째예시값": series.iloc[0],
        }
    )

# 컬럼별 정보 리스트를 DataFrame으로 변환합니다.
data_dictionary = pd.DataFrame(dictionary_rows)

# 완성된 데이터 사전을 출력합니다.
print("\n=== 7. 데이터 사전 ===")
print(data_dictionary)

# 데이터 사전을 CSV 파일로 저장합니다.
data_dictionary.to_csv(
    "applicants_data_dictionary.csv",
    index=False,
    encoding="utf-8-sig",
)

# 전체 지원자 수를 구합니다.
applicant_count = applicants_df.shape[0]

# 전체 컬럼 수를 구합니다.
column_count = applicants_df.shape[1]

# 지원직무 종류 수를 구합니다.
job_type_count = applicants_df["지원직무"].nunique()

# 코딩테스트 평균을 구합니다.
coding_average = applicants_df["코딩테스트"].mean()

# 데이터 점검 요약 제목을 출력합니다.
print("\n=== 8. 데이터 점검 요약 ===")

# 전체 지원자 수를 출력합니다.
print("전체 지원자 수:", applicant_count)

# 전체 컬럼 수를 출력합니다.
print("전체 컬럼 수:", column_count)

# 지원직무 종류 수를 출력합니다.
print("지원직무 종류 수:", job_type_count)

# 코딩테스트 평균을 소수 둘째 자리까지 출력합니다.
print(f"코딩테스트 평균: {coding_average:.2f}")

# 데이터 사전 저장 완료 메시지를 출력합니다.
print("\napplicants_data_dictionary.csv 저장 완료")

# 현재 분석 범위가 데이터 점검 단계임을 출력합니다.
print("현재 단계에서는 데이터 구조와 통계만 확인했으며, 정제 작업은 수행하지 않았다.")
