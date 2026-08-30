# ============================================================
# AI휴먼 11일차 Application 과제 풀이
# 주제: 사내 교육 평가 데이터 전처리
# ============================================================

# 폴더와 파일 경로 처리를 위해 os 모듈을 불러옵니다.
import os

# DataFrame 처리를 위해 pandas를 pd라는 별칭으로 불러옵니다.
import pandas as pd


# ------------------------------------------------------------
# 과제용 원본 CSV 파일 생성
# ------------------------------------------------------------

# 파일을 저장할 폴더를 지정합니다.
assets_dir = "./assets"

# 폴더가 없으면 생성합니다.
os.makedirs(assets_dir, exist_ok=True)

# 원본 파일의 경로를 지정합니다.
raw_path = os.path.join(assets_dir, "day11_training_raw.csv")

# 정제 파일의 경로를 지정합니다.
clean_path = os.path.join(assets_dir, "day11_training_clean.csv")

# 사내 교육 평가 데이터를 딕셔너리로 작성합니다.
training_data = {
    "사번": ["E101", "E102", "E103", "E104", "E105", "E102", "E106", "E107"],
    "부서": ["개발", "기획", None, "마케팅", "개발", "기획", "개발", "마케팅"],
    "과정": ["Python", "데이터분석", "Python", "데이터분석", "AI", "데이터분석", "AI", "Python"],
    "평가점수": ["88", "92", "76", "미응시", "95", "92", "84", None],
    "강사": ["김강사", "이강사", "김강사", "이강사", None, "이강사", "박강사", "김강사"],
}

# 딕셔너리를 원본 DataFrame으로 변환합니다.
source_df = pd.DataFrame(training_data)

# 원본 DataFrame을 CSV 파일로 저장합니다.
source_df.to_csv(raw_path, index=False, encoding="utf-8-sig")


# ------------------------------------------------------------
# 원본 데이터 읽기
# ------------------------------------------------------------

# 원본 CSV 파일을 읽습니다.
df = pd.read_csv(raw_path, encoding="utf-8-sig")

# 전처리 전 비교를 위해 복사본을 만듭니다.
before_df = df.copy()

# 전처리 전 행 수를 계산합니다.
rows_before = before_df.shape[0]

# 전처리 전 전체 결측치 수를 계산합니다.
missing_before = before_df.isna().sum().sum()

# 전처리 전 중복 행 수를 계산합니다.
duplicates_before = before_df.duplicated().sum()

# 원본 dtype을 출력합니다.
print("\n[원본 dtype]")
print(before_df.dtypes)

# 원본 결측치 수를 출력합니다.
print("\n[원본 결측치]")
print(before_df.isna().sum())

# 원본 중복 행 수를 출력합니다.
print("\n[원본 중복 행 수]")
print(duplicates_before)


# ------------------------------------------------------------
# loc와 iloc 조회
# ------------------------------------------------------------

# 데이터분석 과정에 참여한 행에서 일부 컬럼을 선택합니다.
data_course_rows = df.loc[
    df["과정"] == "데이터분석",
    ["사번", "부서", "평가점수"],
]

# loc 조회 결과를 출력합니다.
print("\n[데이터분석 과정 참여자]")
print(data_course_rows)

# 마지막 3행과 앞 3열을 위치 기준으로 선택합니다.
last_rows = df.iloc[-3:, 0:3]

# iloc 조회 결과를 출력합니다.
print("\n[마지막 3행, 앞 3열]")
print(last_rows)


# ------------------------------------------------------------
# 평가점수 숫자 변환
# ------------------------------------------------------------

# 평가점수를 숫자로 변환하고 변환할 수 없는 값은 NaN으로 바꿉니다.
df["평가점수"] = pd.to_numeric(df["평가점수"], errors="coerce")

# 숫자 변환 후 평가점수 결측치 개수를 계산합니다.
score_missing_after_conversion = df["평가점수"].isna().sum()

# 숫자 변환 직후 결측치 개수를 출력합니다.
print("\n[숫자 변환 후 평가점수 결측치]")
print(score_missing_after_conversion)


# ------------------------------------------------------------
# 결측치 처리
# ------------------------------------------------------------

# 평가점수의 중앙값을 계산합니다.
score_median = df["평가점수"].median()

# 평가점수 결측치를 중앙값으로 대체합니다.
df["평가점수"] = df["평가점수"].fillna(score_median)

# 부서 컬럼의 최빈값을 계산합니다.
department_mode = df["부서"].mode()[0]

# 부서 결측치를 최빈값으로 대체합니다.
df["부서"] = df["부서"].fillna(department_mode)

# 강사 결측치를 미배정으로 대체합니다.
df["강사"] = df["강사"].fillna("미배정")


# ------------------------------------------------------------
# 중복 제거와 Index 정리
# ------------------------------------------------------------

# 완전히 동일한 중복 행을 제거합니다.
df = df.drop_duplicates()

# Index를 다시 0부터 정리합니다.
df = df.reset_index(drop=True)

# 평가점수를 정수형으로 변환합니다.
df["평가점수"] = df["평가점수"].astype("int64")


# ------------------------------------------------------------
# 조건 조회
# ------------------------------------------------------------

# 평가점수가 85점 이상인 참여 기록을 선택합니다.
high_score_rows = df.loc[
    df["평가점수"] >= 85,
    ["사번", "부서", "과정", "평가점수"],
]

# 85점 이상 기록을 출력합니다.
print("\n[평가점수 85점 이상]")
print(high_score_rows)


# ------------------------------------------------------------
# 전처리 전후 비교
# ------------------------------------------------------------

# 전처리 후 행 수를 계산합니다.
rows_after = df.shape[0]

# 전처리 후 전체 결측치 수를 계산합니다.
missing_after = df.isna().sum().sum()

# 전처리 후 중복 행 수를 계산합니다.
duplicates_after = df.duplicated().sum()

# 전처리 전후 비교표를 DataFrame으로 작성합니다.
comparison_df = pd.DataFrame(
    {
        "점검항목": ["행 수", "전체 결측치", "중복 행"],
        "전처리전": [rows_before, missing_before, duplicates_before],
        "전처리후": [rows_after, missing_after, duplicates_after],
    }
)

# 비교표를 출력합니다.
print("\n[전처리 전후 비교]")
print(comparison_df)

# 최종 dtype을 출력합니다.
print("\n[최종 dtype]")
print(df.dtypes)


# ------------------------------------------------------------
# 정제 데이터 저장
# ------------------------------------------------------------

# 정제한 DataFrame을 새로운 CSV 파일로 저장합니다.
df.to_csv(clean_path, index=False, encoding="utf-8-sig")

# 저장 경로를 출력합니다.
print("\n[저장 완료]")
print(clean_path)
