# ============================================================
# AI휴먼 과정 - 7일차 실습 코드
# 주제: 파일 입출력, 예외 처리, 모듈, import
# 파일명: day7_ex.py
# ============================================================

# 표준 라이브러리의 csv 모듈을 가져옵니다.
import csv

# pathlib 모듈에서 Path 클래스를 가져옵니다.
from pathlib import Path


# ------------------------------------------------------------
# 1. 실습 폴더와 파일 경로 준비
# ------------------------------------------------------------

# 현재 실행 위치를 기준으로 day7_data 폴더 경로를 만듭니다.
DATA_DIR = Path("day7_data")

# day7_data 폴더가 없으면 새로 만듭니다.
DATA_DIR.mkdir(exist_ok=True)

# 텍스트 파일 경로를 만듭니다.
MEMO_PATH = DATA_DIR / "study_memo.txt"

# CSV 파일 경로를 만듭니다.
SCORE_PATH = DATA_DIR / "scores.csv"

# 존재하지 않는 파일을 읽는 예외 실습용 경로를 만듭니다.
MISSING_PATH = DATA_DIR / "missing.txt"

# 실습 폴더 위치를 화면에 출력합니다.
print("[실습 폴더]", DATA_DIR.resolve())


# ------------------------------------------------------------
# 2. 텍스트 파일 새로 쓰기 - w 모드
# ------------------------------------------------------------

# 처음 저장할 문자열 데이터를 준비합니다.
first_text = "AI휴먼 7일차 학습 기록\n파일 입출력을 학습합니다.\n"

# MEMO_PATH 파일을 쓰기 모드로 엽니다.
with open(MEMO_PATH, "w", encoding="utf-8") as file:
    # 준비한 문자열을 파일에 저장합니다.
    file.write(first_text)

# 파일 저장 완료 메시지를 출력합니다.
print("\n[1] 텍스트 파일 저장 완료")


# ------------------------------------------------------------
# 3. 텍스트 파일 이어 쓰기 - a 모드
# ------------------------------------------------------------

# 기존 파일 뒤에 추가할 문자열을 준비합니다.
append_text = "예외 처리와 모듈도 함께 학습합니다.\n"

# MEMO_PATH 파일을 이어 쓰기 모드로 엽니다.
with open(MEMO_PATH, "a", encoding="utf-8") as file:
    # 기존 내용 뒤에 문자열을 추가합니다.
    file.write(append_text)

# 이어 쓰기 완료 메시지를 출력합니다.
print("[2] 텍스트 파일 내용 추가 완료")


# ------------------------------------------------------------
# 4. 텍스트 파일 전체 읽기 - read()
# ------------------------------------------------------------

# MEMO_PATH 파일을 읽기 모드로 엽니다.
with open(MEMO_PATH, "r", encoding="utf-8") as file:
    # 파일의 전체 내용을 문자열로 읽습니다.
    content = file.read()

# 읽은 전체 내용을 화면에 출력합니다.
print("\n[3] 파일 전체 읽기")

# content 변수의 내용을 출력합니다.
print(content)


# ------------------------------------------------------------
# 5. 텍스트 파일을 한 줄씩 읽기
# ------------------------------------------------------------

# 줄 번호를 보여주기 위한 안내 문구를 출력합니다.
print("[4] 파일 한 줄씩 읽기")

# MEMO_PATH 파일을 읽기 모드로 엽니다.
with open(MEMO_PATH, "r", encoding="utf-8") as file:
    # 파일 객체를 반복하면 한 줄씩 가져올 수 있습니다.
    for line_number, line in enumerate(file, start=1):
        # strip()으로 줄 끝의 줄바꿈 문자를 제거합니다.
        clean_line = line.strip()

        # 줄 번호와 내용을 함께 출력합니다.
        print(f"{line_number}번째 줄: {clean_line}")


# ------------------------------------------------------------
# 6. FileNotFoundError 예외 처리
# ------------------------------------------------------------

# 예외 처리 실습의 시작을 알립니다.
print("\n[5] 존재하지 않는 파일 읽기")

# 오류가 발생할 가능성이 있는 코드를 try 블록에 작성합니다.
try:
    # 실제로 존재하지 않는 파일을 읽기 모드로 엽니다.
    with open(MISSING_PATH, "r", encoding="utf-8") as file:
        # 파일이 열렸다면 전체 내용을 읽습니다.
        missing_content = file.read()

        # 읽은 내용을 출력합니다.
        print(missing_content)

# 파일이 없을 때 FileNotFoundError를 처리합니다.
except FileNotFoundError:
    # 사용자가 이해하기 쉬운 메시지를 출력합니다.
    print("파일을 찾을 수 없습니다. 파일 경로를 확인해 주세요.")


# ------------------------------------------------------------
# 7. ValueError 예외 처리
# ------------------------------------------------------------

# 숫자로 바꿀 수 없는 문자열을 준비합니다.
score_text = "90점"

# 값 변환 예외 처리 실습을 시작합니다.
print("\n[6] 문자열을 정수로 변환")

# int() 변환 과정에서 오류가 발생할 수 있으므로 try를 사용합니다.
try:
    # 문자열을 정수로 변환하려고 시도합니다.
    score = int(score_text)

# 숫자 형식이 아니면 ValueError가 발생합니다.
except ValueError:
    # 오류 원인을 사용자가 알 수 있도록 안내합니다.
    print(f"'{score_text}'은 정수로 변환할 수 없습니다.")


# ------------------------------------------------------------
# 8. try-except-else-finally 실행 흐름
# ------------------------------------------------------------

# 정상적으로 정수 변환이 가능한 문자열을 준비합니다.
number_text = "100"

# 실행 흐름 확인을 위한 제목을 출력합니다.
print("\n[7] try-except-else-finally")

# 오류가 발생할 수 있는 변환 코드를 실행합니다.
try:
    # 문자열을 정수로 변환합니다.
    number = int(number_text)

# 정수 변환에 실패하면 이 블록이 실행됩니다.
except ValueError:
    # 변환 실패 메시지를 출력합니다.
    print("숫자 변환에 실패했습니다.")

# 예외가 발생하지 않았을 때 else 블록이 실행됩니다.
else:
    # 정상적으로 변환된 숫자를 출력합니다.
    print("숫자 변환 성공:", number)

# 예외 발생 여부와 관계없이 finally 블록이 실행됩니다.
finally:
    # 작업 종료 메시지를 출력합니다.
    print("숫자 변환 작업 종료")


# ------------------------------------------------------------
# 9. 파일 저장 기능을 함수로 분리
# ------------------------------------------------------------

# 텍스트를 파일에 저장하는 함수를 정의합니다.
def save_text(path, text):
    # 파일을 쓰기 모드로 엽니다.
    with open(path, "w", encoding="utf-8") as file:
        # 전달받은 문자열을 파일에 저장합니다.
        file.write(text)


# 파일을 읽는 함수를 정의합니다.
def read_text(path):
    # 파일이 없을 수 있으므로 try 블록을 사용합니다.
    try:
        # 파일을 읽기 모드로 엽니다.
        with open(path, "r", encoding="utf-8") as file:
            # 파일 전체 내용을 읽어서 반환합니다.
            return file.read()

    # 파일이 없을 때 예외를 처리합니다.
    except FileNotFoundError:
        # 실패를 나타내기 위해 None을 반환합니다.
        return None


# 함수 실습용 파일 경로를 만듭니다.
FUNCTION_PATH = DATA_DIR / "function_memo.txt"

# save_text() 함수를 호출해 내용을 저장합니다.
save_text(FUNCTION_PATH, "함수로 파일 저장하기\n")

# read_text() 함수를 호출해 내용을 읽습니다.
function_result = read_text(FUNCTION_PATH)

# 함수 실행 결과 제목을 출력합니다.
print("\n[8] 함수로 파일 처리")

# 읽은 결과를 출력합니다.
print(function_result)


# ------------------------------------------------------------
# 10. CSV 파일 쓰기 - csv 모듈
# ------------------------------------------------------------

# CSV에 저장할 학생 데이터를 리스트로 준비합니다.
students = [
    ["name", "score"],
    ["김민수", 88],
    ["이서연", 93],
    ["박지훈", 76],
    ["최유진", 85],
]

# SCORE_PATH 파일을 CSV 쓰기 모드로 엽니다.
with open(SCORE_PATH, "w", newline="", encoding="utf-8-sig") as file:
    # CSV 데이터를 작성할 writer 객체를 만듭니다.
    writer = csv.writer(file)

    # 여러 행을 한 번에 CSV 파일에 저장합니다.
    writer.writerows(students)

# CSV 저장 완료 메시지를 출력합니다.
print("[9] CSV 파일 저장 완료")


# ------------------------------------------------------------
# 11. CSV 파일 읽기 - csv.reader()
# ------------------------------------------------------------

# CSV 읽기 결과를 저장할 빈 리스트를 만듭니다.
score_values = []

# CSV 파일을 읽기 모드로 엽니다.
with open(SCORE_PATH, "r", encoding="utf-8-sig") as file:
    # CSV 파일을 행 단위로 읽는 reader 객체를 만듭니다.
    reader = csv.reader(file)

    # 첫 번째 행의 헤더를 읽습니다.
    header = next(reader)

    # 나머지 데이터 행을 한 줄씩 반복합니다.
    for row in reader:
        # 첫 번째 열의 학생 이름을 가져옵니다.
        name = row[0]

        # 두 번째 열의 점수 문자열을 정수로 변환합니다.
        score = int(row[1])

        # 변환한 점수를 리스트에 추가합니다.
        score_values.append(score)

        # 학생 이름과 점수를 화면에 출력합니다.
        print(f"{name}: {score}점")

# 헤더 내용을 출력합니다.
print("\n[10] CSV 헤더:", header)

# 점수 합계를 계산합니다.
total_score = sum(score_values)

# 학생 수를 계산합니다.
student_count = len(score_values)

# 학생 수가 0보다 큰지 확인합니다.
if student_count > 0:
    # 평균 점수를 계산합니다.
    average_score = total_score / student_count

    # 평균 점수를 소수점 둘째 자리까지 출력합니다.
    print(f"평균 점수: {average_score:.2f}점")

# 학생 데이터가 없을 때를 처리합니다.
else:
    # 데이터가 없다는 메시지를 출력합니다.
    print("계산할 학생 데이터가 없습니다.")


# ------------------------------------------------------------
# 12. 안전한 CSV 읽기 함수를 작성
# ------------------------------------------------------------

# CSV 파일을 안전하게 읽는 함수를 정의합니다.
def load_score_csv(path):
    # 성공한 데이터 행을 저장할 리스트를 만듭니다.
    result = []

    # 파일과 데이터 형식 오류가 발생할 수 있으므로 try를 사용합니다.
    try:
        # 전달받은 CSV 파일을 읽기 모드로 엽니다.
        with open(path, "r", encoding="utf-8-sig") as file:
            # csv.reader 객체를 만듭니다.
            reader = csv.reader(file)

            # 첫 번째 행을 헤더로 읽습니다.
            next(reader)

            # 데이터 행을 반복해서 읽습니다.
            for row_number, row in enumerate(reader, start=2):
                # 열이 2개보다 적으면 잘못된 행으로 판단합니다.
                if len(row) < 2:
                    # 잘못된 행 번호를 출력합니다.
                    print(f"{row_number}행: 열 개수가 부족하여 건너뜁니다.")

                    # 다음 반복으로 이동합니다.
                    continue

                # 학생 이름을 가져옵니다.
                name = row[0].strip()

                # 점수 문자열을 정수로 변환합니다.
                score = int(row[1])

                # 정상 데이터를 튜플 형태로 저장합니다.
                result.append((name, score))

    # 파일을 찾을 수 없을 때 처리합니다.
    except FileNotFoundError:
        # 파일 경로 오류 메시지를 출력합니다.
        print("CSV 파일을 찾을 수 없습니다:", path)

    # 점수 변환에 실패했을 때 처리합니다.
    except ValueError as error:
        # 숫자 형식 오류 메시지를 출력합니다.
        print("점수 데이터 형식 오류:", error)

    # 예상하지 못한 인코딩 문제가 발생했을 때 처리합니다.
    except UnicodeDecodeError:
        # 인코딩 확인 메시지를 출력합니다.
        print("파일 인코딩을 확인해 주세요.")

    # 함수의 최종 결과 리스트를 반환합니다.
    return result


# 안전한 CSV 읽기 함수를 호출합니다.
safe_scores = load_score_csv(SCORE_PATH)

# 안전한 CSV 읽기 결과 제목을 출력합니다.
print("\n[11] 안전한 CSV 읽기 결과")

# 함수에서 반환된 데이터를 출력합니다.
print(safe_scores)


# ------------------------------------------------------------
# 13. 실습 마무리
# ------------------------------------------------------------

# 오늘 실습에서 생성된 파일 목록을 확인합니다.
print("\n[12] 생성된 파일 목록")

# day7_data 폴더 안의 모든 항목을 정렬해서 반복합니다.
for path in sorted(DATA_DIR.iterdir()):
    # 각 파일의 이름을 출력합니다.
    print("-", path.name)

# 전체 실습이 끝났음을 알립니다.
print("\n7일차 실습이 완료되었습니다.")
