import pandas as pd


file_name = "test22.xlsx"
df = pd.read_excel(file_name)


# 판다스에서 날짜를 dd-mm-yy로 치환하는 이슈가 있기 에 하기 작업을 통해 날짜를 고정해야함 

#날짜 픽스 작업
#문자열로 변환 후 연도 앞에 '20' 붙이기 → 25 → 2025
df['DateTime'] = df['DateTime'].astype(str).str.replace(r'^(\d{2})-', r'20\1-', regex=True)
#다시 datetime 형식으로 변환
df['DateTime'] = pd.to_datetime(df['DateTime'], format="%Y-%m-%d %H:%M:%S")



# 09:00~ 18:00외 데이터를 날리기 위한 필터링
df = df[(df['DateTime'].dt.time >= pd.to_datetime("09:00:00").time()) &
        (df['DateTime'].dt.time < pd.to_datetime("18:30:00").time())]


# 모든 인스턴스의 메모리 리소스 사용률 평균 값 구하기

len(df.columns)
hostname_count = len(df.columns) -1   #date를 제외한 인스턴스 수
hostname_count

df['sum'] = df.select_dtypes(include=['float64', 'int64']).sum(axis=1)
df['average'] = df['sum'] / hostname_count



#09:00, 09:30, 10:00 세 개씩의 평균 값 구하는 함수수
def generate_hour_groups(row):
    ts = pd.to_datetime(row['DateTime'])  # ← 여기서 변환 보장!
    groups = []
    floor_prev = (ts - pd.Timedelta(minutes=60)).replace(minute=0, second=0)
    floor_curr = ts.replace(minute=0, second=0)

    if ts.minute == 0:
        groups = [floor_prev, floor_curr]
    else:
        groups = [floor_curr]

    return pd.DataFrame({
        'HourGroup': groups,
        'average': row['average']
    })

# 모든 행에 대해 중첩 그룹 생성
expanded_df = pd.concat([generate_hour_groups(row) for _, row in df.iterrows()], ignore_index=True)

# 평균 계산
df = expanded_df.groupby('HourGroup')['average'].mean().reset_index()

# 08:00를 떼어내기 위함
df = df[df['HourGroup'].dt.time != pd.to_datetime("08:00:00").time()]



# HourGroup을 datetime 형식으로 변환
df['HourGroup'] = pd.to_datetime(df['HourGroup'])

# 날짜와 시간 분리
df['Date'] = df['HourGroup'].dt.date
df['Hour'] = df['HourGroup'].dt.strftime('%H:%M')

# 피벗 테이블: 날짜를 행, 시간을 열로 배치
pivot_df = df.pivot(index='Date', columns='Hour', values='average')

# 저장
pivot_df.to_excel("final_" + file_name)