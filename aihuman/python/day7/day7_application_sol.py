# ============================================================
# AI휴먼 과정 - 7일차 Application 과제 풀이
# 파일명: day7_application_sol.py
# ============================================================

# CSV 파일 처리를 위해 csv 모듈을 가져옵니다.
import csv

# 파일과 폴더 경로 처리를 위해 Path 클래스를 가져옵니다.
from pathlib import Path

# 과제용 폴더 경로를 만듭니다.
DATA_DIR = Path("day7_application_data")

# 폴더가 없으면 새로 만듭니다.
DATA_DIR.mkdir(exist_ok=True)

# 성적 CSV 파일 경로를 만듭니다.
CSV_PATH = DATA_DIR / "student_scores.csv"


# 샘플 CSV 파일을 만드는 함수를 정의합니다.
def create_sample_csv(path):
    # 저장할 샘플 학생 데이터를 준비합니다.
    rows = [
        ["name", "score"],
        ["김민수", 88],
        ["이서연", 93],
        ["박지훈", 76],
        ["최유진", 85],
    ]

    # 전달받은 경로의 파일을 쓰기 모드로 엽니다.
    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        # CSV writer 객체를 만듭니다.
        writer = csv.writer(file)

        # 준비한 모든 행을 파일에 저장합니다.
        writer.writerows(rows)


# CSV 성적을 안전하게 읽는 함수를 정의합니다.
def load_scores(path):
    # 정상 데이터를 저장할 빈 리스트를 만듭니다.
    result = []

    # 파일 또는 데이터 형식 오류가 발생할 수 있으므로 try를 사용합니다.
    try:
        # CSV 파일을 읽기 모드로 엽니다.
        with open(path, "r", encoding="utf-8-sig") as file:
            # CSV reader 객체를 만듭니다.
            reader = csv.reader(file)

            # 첫 번째 행의 헤더를 읽습니다.
            header = next(reader)

            # 헤더 내용을 확인용으로 출력합니다.
            print("CSV 헤더:", header)

            # 나머지 데이터 행을 반복합니다.
            for row in reader:
                # 첫 번째 열에서 이름을 가져옵니다.
                name = row[0].strip()

                # 두 번째 열의 점수 문자열을 정수로 변환합니다.
                score = int(row[1])

                # 정상 데이터를 튜플로 리스트에 추가합니다.
                result.append((name, score))

    # 파일을 찾을 수 없을 때 처리합니다.
    except FileNotFoundError:
        # 파일이 없음을 안내합니다.
        print("성적 파일을 찾을 수 없습니다.")

    # 숫자 변환에 실패했을 때 처리합니다.
    except ValueError:
        # 점수 형식 오류를 안내합니다.
        print("점수는 숫자로 입력되어야 합니다.")

    # 정상적으로 읽은 데이터 리스트를 반환합니다.
    return result


# CSV 파일이 아직 없으면 샘플 파일을 만듭니다.
if not CSV_PATH.exists():
    # 샘플 CSV 파일을 생성합니다.
    create_sample_csv(CSV_PATH)

# 성적 CSV를 읽는 함수를 호출합니다.
scores = load_scores(CSV_PATH)

# 정상 데이터가 있는지 확인합니다.
if len(scores) > 0:
    # 출력 제목을 표시합니다.
    print("\n[학생별 점수]")

    # 학생 데이터를 하나씩 반복합니다.
    for name, score in scores:
        # 학생 이름과 점수를 출력합니다.
        print(f"{name}: {score}점")

    # 모든 점수의 합계를 계산합니다.
    total = sum(score for name, score in scores)

    # 평균 점수를 계산합니다.
    average = total / len(scores)

    # 평균 점수를 소수점 둘째 자리까지 출력합니다.
    print(f"\n평균 점수: {average:.2f}점")

# 정상 데이터가 하나도 없을 때 처리합니다.
else:
    # 계산할 데이터가 없다는 메시지를 출력합니다.
    print("계산할 데이터가 없습니다.")
