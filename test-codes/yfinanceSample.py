from pandas_datareader import data as pdr
from matplotlib import rc
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

yf.pdr_override() # 크롤링으로 데이터 가져오기

# 이마트 종목코드 : 139480.KS
df_stock = pdr.get_data_yahoo('139480.KS', start = '2011-01-01', end = '2023-12-31')

# 이마트 종목코드 : 139480.KS, KOSPI 지수 : ^KS11
df = pdr.get_data_yahoo(['139480.KS', '^KS11'], start = '2018-01-01', end = '2023-12-31')

df = df.reset_index() # 날짜를 컬럼으로 변경
df = df[['Date', 'Close']]
df.columns = ['date', 'price', 'kospi지수']

df.date = pd.to_datetime(df.date) # 날짜를 datetime 형식으로 변경
df['date'] = df['date'].dt.strftime('%Y-%m')

# 월별 평균 주가와 코스피 지수
df1 = pd.DataFrame(df.groupby('date')['price'].mean())
df1 = df1.reset_index()
df2 = pd.DataFrame(df.groupby('date')['kospi지수'].mean())
df2 = df2.reset_index()
df = df1.merge(df2, how = 'left')


# MinMaxScaler를 이용해 데이터 정규화하기
# MinMaxScaler : 데이터의 최솟값, 최댓값을 이용해 데이터 값을 0~1 사이로 변환
df = df.set_index('date') # date를 index로 변경
scaler = MinMaxScaler() 
scaler.fit(df) 
scaled = scaler.transform(df) # 데이터 반환
df_scaled = pd.DataFrame(scaled, columns = ['pricemm', 'kospimm'])
df = df.reset_index('date') 
df_scaled.insert(0, 'date', df['date'])

df = df.merge(df_scaled, how = 'left')
# df.head()

# 그래프
plt.figure(figsize = (16, 5))
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['font.size'] = 12

sns.lineplot(data=df, x='date', y='pricemm', label='price_mm') 
sns.lineplot(data=df, x='date', y='kospimm', label='kospi_mm')

plt.title('주가와 코스피 지수 월별 평균 비교')
plt.xticks(rotation = 45) # x축 눈금 라벨 회전

plt.show()