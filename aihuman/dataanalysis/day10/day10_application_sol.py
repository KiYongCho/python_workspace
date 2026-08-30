# Day 10 Application 과제 풀이: 온라인 주문 데이터 기초 탐색

# pandas 라이브러리를 pd라는 별칭으로 불러옵니다.
import pandas as pd


# 온라인 주문 데이터를 딕셔너리로 준비합니다.
order_data = {
    # 주문번호 데이터를 저장합니다.
    "주문번호": ["O001", "O002", "O003", "O004", "O005", "O006", "O007", "O008"],
    # 주문 채널 데이터를 저장합니다.
    "채널": ["모바일", "웹", "모바일", "웹", "모바일", "앱", "앱", "웹"],
    # 상품분류 데이터를 저장합니다.
    "상품분류": ["전자기기", "생활용품", "패션", "전자기기", "생활용품", "패션", "전자기기", "패션"],
    # 수량 데이터를 저장합니다.
    "수량": [1, 3, 2, 1, 5, 1, 2, 3],
    # 주문금액 데이터를 저장합니다.
    "주문금액": [120000, 45000, 78000, 210000, 65000, 52000, 330000, 99000],
}

# 딕셔너리를 DataFrame으로 변환합니다.
source_df = pd.DataFrame(order_data)

# DataFrame을 CSV 파일로 저장합니다.
source_df.to_csv("online_orders.csv", index=False, encoding="utf-8-sig")

# CSV 파일을 다시 읽어 주문 DataFrame을 만듭니다.
orders_df = pd.read_csv("online_orders.csv", encoding="utf-8-sig")

# 데이터 타입과 전체 데이터를 확인하는 제목을 출력합니다.
print("=== 1. DataFrame 확인 ===")

# orders_df의 Python 객체 타입을 출력합니다.
print("객체 타입:", type(orders_df))

# 전체 주문 데이터를 출력합니다.
print(orders_df)

# 구조 확인 제목을 출력합니다.
print("\n=== 2. 데이터 구조 ===")

# 행과 열의 크기를 출력합니다.
print("shape:", orders_df.shape)

# 차원 수를 출력합니다.
print("ndim:", orders_df.ndim)

# 전체 원소 수를 출력합니다.
print("size:", orders_df.size)

# 컬럼 목록을 출력합니다.
print("columns:", list(orders_df.columns))

# 각 컬럼의 dtype을 출력합니다.
print("\ndtypes")
print(orders_df.dtypes)

# 필요한 3개 컬럼만 선택합니다.
selected_df = orders_df[["주문번호", "상품분류", "주문금액"]]

# 선택한 DataFrame을 출력합니다.
print("\n=== 3. 필요한 컬럼 선택 ===")
print(selected_df)

# 주문금액 한 컬럼을 Series로 선택합니다.
amount = orders_df["주문금액"]

# 주문금액 Series의 객체 타입을 출력합니다.
print("\n=== 4. 주문금액 Series ===")
print("객체 타입:", type(amount))

# 주문금액 합계를 출력합니다.
print("합계:", amount.sum())

# 주문금액 평균을 소수 둘째 자리까지 출력합니다.
print(f"평균: {amount.mean():.2f}")

# 주문금액 중앙값을 출력합니다.
print("중앙값:", amount.median())

# 주문금액 최솟값을 출력합니다.
print("최솟값:", amount.min())

# 주문금액 최댓값을 출력합니다.
print("최댓값:", amount.max())

# 숫자형 전체 컬럼의 기초통계를 출력합니다.
print("\n=== 5. describe() 결과 ===")
print(orders_df.describe())

# 채널별 주문 건수를 출력합니다.
print("\n=== 6. 채널별 주문 건수 ===")
print(orders_df["채널"].value_counts())

# 상품분류의 고유값 목록을 출력합니다.
print("\n=== 7. 상품분류 구성 ===")
print("고유값:", orders_df["상품분류"].unique())

# 상품분류의 고유값 개수를 출력합니다.
print("고유값 개수:", orders_df["상품분류"].nunique())

# usecols를 이용해 필요한 두 컬럼만 CSV에서 다시 읽습니다.
channel_amount_df = pd.read_csv(
    "online_orders.csv",
    encoding="utf-8-sig",
    usecols=["채널", "주문금액"],
)

# usecols 적용 결과를 출력합니다.
print("\n=== 8. usecols 적용 결과 ===")
print(channel_amount_df)

# 가장 많이 사용된 채널의 이름을 가져옵니다.
top_channel = orders_df["채널"].value_counts().index[0]

# 마지막 요약 제목을 출력합니다.
print("\n=== 9. 데이터 점검 요약 ===")

# 데이터 크기를 한 줄로 요약해 출력합니다.
print(f"데이터는 {orders_df.shape[0]}행, {orders_df.shape[1]}열입니다.")

# 주문금액 평균을 한 줄로 요약해 출력합니다.
print(f"평균 주문금액은 {amount.mean():,.0f}원입니다.")

# 가장 많이 사용된 채널을 한 줄로 요약해 출력합니다.
print(f"가장 많이 사용된 주문 채널은 '{top_channel}'입니다.")
