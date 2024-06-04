import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from pandas_datareader import data as pdr

yf.pdr_override()

df = pdr.get_data_yahoo("005930.KS")
df

close = df['Close']
start_date = '2024-05-17'
end_date = '2024-06-05'
close[start_date:end_date].plot();

df1 = close[start_date:end_date]
df1

df1_norm = (df1 - df1.min()) / (df1.max() - df1.min())
df1_norm

# 윈도우 사이즈, 몇일간의 패턴을 확인할 것인지
window_size = len(df1)

# 예측 기간
next_date = 5

# 검색 횟수
moving_cnt = len(close) - window_size - next_date - 1

def cosine_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

sim_list = []

for i in range(moving_cnt):
    target = close[i:i+window_size]

    target_norm = (target - target.min()) / (target.max() - target.min())

    # 코사인 유사도 저장
    cos_similarity = cosine_similarity(df1_norm, target_norm)

    # 코사인 유사도 <- i(인덱스), 시계열데이터 함께 저장
    sim_list.append(cos_similarity)

top_similarities = pd.Series(sim_list).sort_values(ascending=False).head(20)
print(top_similarities)

idx = 5624

top_ = close[idx:idx+window_size+next_date]
top_norm = (top_ - top_.min()) / (top_.max() - top_.min())

plt.plot(df1_norm.values, label='df1')
plt.plot(top_norm.values, label='target')
plt.axvline(x=len(df1_norm)-1, c='r', linestyle='--')
plt.axvspan(len(df1_norm.values)-1, len(top_norm.values)-1, facecolor='yellow', alpha=0.3)
plt.legend()
plt.show()