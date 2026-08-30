# ============================================================
# AI휴먼 과정 - 7일차 Challenge 과제 풀이
# 파일명: day7_challenge_sol.py
# ============================================================

# 파일과 폴더 경로를 편리하게 처리하기 위해 Path 클래스를 가져옵니다.
from pathlib import Path

# 직접 만든 CSV 처리 모듈을 가져옵니다.
import day7_challenge_utils

# Challenge 과제용 데이터 폴더 경로를 만듭니다.
DATA_DIR = Path("day7_challenge_data")

# 폴더가 없으면 새로 만듭니다.
DATA_DIR.mkdir(exist_ok=True)

# 처리할 CSV 파일 경로를 만듭니다.
CSV_PATH = DATA_DIR / "challenge_scores.csv"

# CSV 파일이 아직 존재하지 않는지 확인합니다.
if not CSV_PATH.exists():
    # 보조 모듈의 함수를 사용해 샘플 CSV 파일을 만듭니다.
    day7_challenge_utils.save_sample_csv(CSV_PATH)

# 보조 모듈의 함수를 사용해 CSV 데이터를 안전하게 읽습니다.
students = day7_challenge_utils.load_score_csv(CSV_PATH)

# 정상 데이터가 하나 이상 있는지 확인합니다.
if len(students) > 0:
    # 학생 튜플에서 점수만 추출해 리스트로 만듭니다.
    scores = [score for name, score in students]

    # 정상 학생 수를 계산합니다.
    student_count = len(students)

    # 점수 합계를 계산합니다.
    total_score = sum(scores)

    # 평균 점수를 계산합니다.
    average_score = total_score / student_count

    # 최고점을 계산합니다.
    max_score = max(scores)

    # 최저점을 계산합니다.
    min_score = min(scores)

    # 정상 학생 수를 출력합니다.
    print(f"정상 학생 수: {student_count}명")

    # 평균 점수를 소수점 둘째 자리까지 출력합니다.
    print(f"평균: {average_score:.2f}점")

    # 최고점을 출력합니다.
    print(f"최고점: {max_score}점")

    # 최저점을 출력합니다.
    print(f"최저점: {min_score}점")

    # PASS 학생 목록 제목을 출력합니다.
    print("\n[PASS 학생]")

    # 모든 정상 학생 데이터를 반복합니다.
    for name, score in students:
        # 점수가 80점 이상인지 확인합니다.
        if score >= 80:
            # PASS 기준을 만족하는 학생만 출력합니다.
            print(f"{name}: {score}점")

# 정상 데이터가 없을 때 처리합니다.
else:
    # 통계 계산이 불가능함을 안내합니다.
    print("정상 학생 데이터가 없어 통계를 계산하지 않습니다.")
