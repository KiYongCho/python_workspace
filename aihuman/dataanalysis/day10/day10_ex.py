# Day 10 실습: Pandas DataFrame 기초
# 목표: CSV 파일을 읽고 데이터 구조와 기초통계를 체계적으로 확인합니다.

# Path는 운영체제에 관계없이 파일 경로를 다루기 위한 표준 라이브러리 클래스입니다.
from pathlib import Path

# pandas를 pd라는 관례적인 별칭으로 불러옵니다.
import pandas as pd


# 실습에서 사용할 CSV 파일 경로를 지정합니다.
DATA_FILE = Path("students.csv")

# 실습 결과로 저장할 데이터 점검표 파일 경로를 지정합니다.
REPORT_FILE = Path("students_data_dictionary.csv")


# 실습용 CSV 파일을 만드는 함수를 정의합니다.
def create_sample_csv():
    # CSV 파일에 저장할 학생 데이터를 딕셔너리 형태로 준비합니다.
    sample_data = {
        # 학생을 구분하기 위한 식별 코드를 리스트로 저장합니다.
        "학생ID": ["S001", "S002", "S003", "S004", "S005", "S006", "S007", "S008"],
        # 학생 이름을 리스트로 저장합니다.
        "이름": ["김민지", "박준호", "이서연", "최도윤", "정하은", "윤지호", "한유진", "오민석"],
        # 학생 전공을 리스트로 저장합니다.
        "전공": ["컴퓨터공학", "경영학", "통계학", "전자공학", "경영학", "컴퓨터공학", "디자인", "전자공학"],
        # Python 평가 점수를 정수 리스트로 저장합니다.
        "Python점수": [88, 76, 95, 82, 91, 69, 84, 90],
        # AI 평가 점수를 정수 리스트로 저장합니다.
        "AI점수": [91, 80, 93, 85, 89, 74, 88, 92],
        # 출석률을 실수 리스트로 저장합니다.
        "출석률": [98.0, 94.5, 100.0, 96.0, 99.0, 91.5, 97.0, 98.5],
    }

    # 준비한 딕셔너리를 DataFrame으로 변환합니다.
    sample_df = pd.DataFrame(sample_data)

    # DataFrame을 UTF-8 BOM이 포함된 CSV 파일로 저장합니다.
    sample_df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

    # 샘플 파일이 생성되었다는 메시지를 출력합니다.
    print(f"[파일 생성] {DATA_FILE.resolve()}")


# 실습용 CSV 파일이 현재 폴더에 존재하지 않는지 확인합니다.
if not DATA_FILE.exists():
    # 파일이 없으면 실습 데이터를 자동으로 생성합니다.
    create_sample_csv()


# CSV 파일을 읽어 DataFrame으로 변환합니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# 구분선을 출력해 실행 결과를 읽기 쉽게 만듭니다.
print("=" * 70)

# 현재 실습 제목을 출력합니다.
print("1. CSV 파일 읽기와 DataFrame 확인")

# df 객체의 실제 Python 타입을 출력합니다.
print("DataFrame 타입:", type(df))

# DataFrame 전체를 출력합니다.
print(df)


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# 앞부분과 뒷부분 확인 실습 제목을 출력합니다.
print("2. head()와 tail()로 데이터 미리보기")

# DataFrame의 처음 5개 행을 출력합니다.
print("\n[처음 5개 행]")
print(df.head())

# DataFrame의 마지막 3개 행을 출력합니다.
print("\n[마지막 3개 행]")
print(df.tail(3))


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# 데이터 구조 확인 실습 제목을 출력합니다.
print("3. shape, ndim, size, columns, index 확인")

# shape의 첫 번째 값인 행 수를 rows 변수에 저장합니다.
rows = df.shape[0]

# shape의 두 번째 값인 열 수를 cols 변수에 저장합니다.
cols = df.shape[1]

# DataFrame의 행 수를 출력합니다.
print("행 수:", rows)

# DataFrame의 열 수를 출력합니다.
print("열 수:", cols)

# DataFrame의 차원 수를 출력합니다.
print("차원 수:", df.ndim)

# DataFrame 전체 원소 개수를 출력합니다.
print("전체 원소 수:", df.size)

# DataFrame 컬럼 이름을 출력합니다.
print("컬럼 목록:", list(df.columns))

# DataFrame 인덱스를 출력합니다.
print("인덱스:", df.index)


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# dtype 확인 실습 제목을 출력합니다.
print("4. 컬럼별 dtype 확인")

# 각 컬럼의 dtype을 출력합니다.
print(df.dtypes)


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# info() 실습 제목을 출력합니다.
print("5. info()로 구조와 Non-Null Count 확인")

# info()는 결과를 직접 출력하므로 print() 없이 호출합니다.
df.info()


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# Series와 DataFrame 선택 차이를 확인하는 제목을 출력합니다.
print("6. 한 컬럼과 여러 컬럼 선택")

# 한 개 컬럼을 선택해 Series 객체로 저장합니다.
python_score = df["Python점수"]

# 한 컬럼 선택 결과의 타입을 출력합니다.
print("한 컬럼 타입:", type(python_score))

# Python점수 Series의 처음 5개 값을 출력합니다.
print(python_score.head())

# 여러 컬럼명을 리스트로 전달해 DataFrame으로 선택합니다.
score_df = df[["이름", "Python점수", "AI점수"]]

# 여러 컬럼 선택 결과의 타입을 출력합니다.
print("\n여러 컬럼 타입:", type(score_df))

# 선택한 여러 컬럼의 앞 5개 행을 출력합니다.
print(score_df.head())


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# 숫자형 기초통계 실습 제목을 출력합니다.
print("7. describe()로 숫자형 기초통계 확인")

# 숫자형 컬럼의 count, mean, std, min, 사분위수, max를 출력합니다.
print(df.describe())


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# Series 집계 메소드 실습 제목을 출력합니다.
print("8. Python점수 Series의 주요 집계값")

# Python점수 합계를 출력합니다.
print("합계:", python_score.sum())

# Python점수 평균을 소수 둘째 자리까지 출력합니다.
print(f"평균: {python_score.mean():.2f}")

# Python점수 중앙값을 출력합니다.
print("중앙값:", python_score.median())

# Python점수 최솟값을 출력합니다.
print("최솟값:", python_score.min())

# Python점수 최댓값을 출력합니다.
print("최댓값:", python_score.max())

# Python점수에서 실제 값이 존재하는 개수를 출력합니다.
print("값의 개수:", python_score.count())


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# 범주형 데이터 확인 실습 제목을 출력합니다.
print("9. 전공 컬럼의 고유값과 빈도 확인")

# 전공의 고유한 값 목록을 출력합니다.
print("고유 전공:", df["전공"].unique())

# 전공의 고유한 값 개수를 출력합니다.
print("전공 종류 수:", df["전공"].nunique())

# 전공별 학생 수를 출력합니다.
print("\n전공별 학생 수")
print(df["전공"].value_counts())


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# read_csv() 인수 활용 실습 제목을 출력합니다.
print("10. read_csv()의 usecols와 nrows 활용")

# CSV에서 이름과 두 점수 컬럼만 읽어 새로운 DataFrame으로 만듭니다.
selected_df = pd.read_csv(
    DATA_FILE,
    encoding="utf-8-sig",
    usecols=["이름", "Python점수", "AI점수"],
)

# 선택된 컬럼만 가진 DataFrame을 출력합니다.
print("\n[필요한 컬럼만 읽기]")
print(selected_df)

# CSV 파일의 처음 3개 데이터 행만 읽습니다.
first_three_df = pd.read_csv(
    DATA_FILE,
    encoding="utf-8-sig",
    nrows=3,
)

# 처음 3개 행만 읽은 결과를 출력합니다.
print("\n[처음 3개 행만 읽기]")
print(first_three_df)


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# 데이터 사전 작성 실습 제목을 출력합니다.
print("11. 데이터 점검표(Data Dictionary) 만들기")

# 컬럼별 점검 결과를 담을 빈 리스트를 생성합니다.
data_dictionary_rows = []

# DataFrame의 모든 컬럼명을 차례대로 반복합니다.
for column in df.columns:
    # 현재 컬럼을 Series로 선택합니다.
    series = df[column]

    # 현재 컬럼의 첫 번째 값을 예시값으로 가져옵니다.
    example_value = series.iloc[0]

    # 현재 컬럼의 정보를 딕셔너리로 만들어 리스트에 추가합니다.
    data_dictionary_rows.append(
        {
            "컬럼명": column,
            "dtype": str(series.dtype),
            "전체행수": len(series),
            "Non-Null개수": series.count(),
            "고유값수": series.nunique(),
            "예시값": example_value,
        }
    )

# 컬럼별 점검 결과 리스트를 DataFrame으로 변환합니다.
data_dictionary = pd.DataFrame(data_dictionary_rows)

# 완성된 데이터 점검표를 화면에 출력합니다.
print(data_dictionary)

# 데이터 점검표를 별도의 CSV 파일로 저장합니다.
data_dictionary.to_csv(REPORT_FILE, index=False, encoding="utf-8-sig")

# 저장된 파일의 절대 경로를 출력합니다.
print(f"\n[점검표 저장 완료] {REPORT_FILE.resolve()}")


# 구분선을 출력합니다.
print("\n" + "=" * 70)

# 실습 완료 메시지를 출력합니다.
print("Day 10 실습 완료: CSV → DataFrame → 구조 확인 → 기초통계 → 데이터 점검표")
