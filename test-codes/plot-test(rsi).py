# 보조지표 - RSI (상대강도지수) 표시 plot Code
# RSI - 30이하 과매도 상태 => 매수점 , 70이상 과매수 상태 => 매도점

import yfinance as yf
import matplotlib.pyplot as plt            # plot 시각표현 library
import pandas_ta as ta                     # rsi 계산 library


# 엔비디아(NVIDIA) 데이터 가져와 1년으로 설정
nvidia = yf.Ticker("NVDA")
data = nvidia.history(period="1y")


# RSI 계산
data.ta.rsi(length=14, append=True)                   # 통상적으로 사용하는 rsi 계산기간 14일, append = True 로 줘 기존 데이터에 rsi컬럼을 새로 생성하여 넣기


# 그래프 그리기
plt.figure(figsize=(10, 5))                                             # 그래프 사이즈 가로 10, 세로 5
plt.plot(data.index, data['RSI_14'], label='RSI', color='red')          # x축 - data.index(날짜), y축 - rsi값 컬럼 , 범례, 색
plt.title('NVIDIA RSI')                                                 
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend(loc='upper left')                                            # 범례 표시 위치
plt.grid(True)                                                          # 격자 표시
plt.show()



# 기간 중 특정 날짜 RSI 표시

date = input("날짜를 입력하세요 (YYYY-MM-DD): ")

# 입력한 날짜에 해당하는 RSI 값 출력
try:
    rsi = data.loc[date, 'RSI_14']                                     # loc[] date 행의 RSI 컬럼값을 가져옴
    print(f"{date}일 RSI : {rsi}")
except KeyError:
    print("해당 날짜의 RSI 데이터가 없습니다.")