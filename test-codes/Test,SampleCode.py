# yfinance sample, test Code

# pip install yfinance
import yfinance as yf


# first sample
# 엔비디아 주식 데이터 다운로드
nvidia = "NVDA"
nvda = yf.Ticker(nvidia)

# 최근 1년 및 5년간 주가 데이터 지정
nvda_data_1y = nvda.history(period="1y")
nvda_data_5y = nvda.history(period="5y")


# 만약 1년전과 5년전에 투자했을 시, 현재 수익률
# 수익률 계산 및 출력(%) 함수
def calbenefit(data):
    start_price = data['Close'][0]              # 시작 시점 종가 (데이터셋에서 Close 컬럼 첫번째, 인덱스 0)
    end_price = data['Close'][-1]               # 현재 종가                             (마지막 인덱스 -1)
    return_rate = ((end_price - start_price) / start_price) * 100
    return print("수익률",return_rate,"%")


# 엔비디아의 1년, 5년 투자수익률 계산
calbenefit(nvda_data_1y)
calbenefit(nvda_data_5y)


# second sample
# AMD 주식 데이터를 다운로드

amd = yf.Ticker("AMD")

# 최근 1년 및 5년간의 주가 데이터 지정
amd_data_1y = amd.history(period="1y")
amd_data_5y = amd.history(period="5y")

# AMD의 1년, 5년 투자수익률 계산
calbenefit(amd_data_1y)
calbenefit(amd_data_5y)
