# ============================================================
# AI휴먼 과정 - 7일차 Basic 과제 풀이
# 파일명: day7_basic_sol.py
# ============================================================

# pathlib 모듈에서 Path 클래스를 가져옵니다.
from pathlib import Path

# 과제용 폴더 경로를 만듭니다.
DATA_DIR = Path("day7_basic_data")

# 폴더가 없으면 새로 만듭니다.
DATA_DIR.mkdir(exist_ok=True)

# 학습 기록 파일 경로를 만듭니다.
FILE_PATH = DATA_DIR / "learning_log.txt"

# 처음 저장할 학습 기록 문자열을 준비합니다.
first_log = (
    "과정명: AI휴먼\n"
    "학습주제: 파일 입출력과 예외 처리\n"
    "핵심 개념: with open()은 파일을 자동으로 닫아준다.\n"
)

# 파일을 쓰기 모드로 엽니다.
with open(FILE_PATH, "w", encoding="utf-8") as file:
    # 처음 학습 기록을 파일에 저장합니다.
    file.write(first_log)

# 기존 파일 뒤에 추가할 복습 내용을 준비합니다.
review_log = "다음에 복습할 내용: try-except\n"

# 파일을 이어 쓰기 모드로 엽니다.
with open(FILE_PATH, "a", encoding="utf-8") as file:
    # 기존 내용 뒤에 복습 내용을 추가합니다.
    file.write(review_log)

# 완성된 파일을 읽기 모드로 엽니다.
with open(FILE_PATH, "r", encoding="utf-8") as file:
    # 파일 전체 내용을 문자열로 읽습니다.
    content = file.read()

# 저장된 파일 위치를 출력합니다.
print("저장 파일:", FILE_PATH.resolve())

# 파일 내용 제목을 출력합니다.
print("\n[학습 기록]")

# 읽은 전체 내용을 출력합니다.
print(content)
