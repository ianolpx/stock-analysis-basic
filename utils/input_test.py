import yfinance as yf
from pandas_datareader import data as pdr


def get_df(code):
  yf.pdr_override()
  df = pdr.get_data_yahoo("005930.KS", "2024-04-01", "2024-05-01")

  return df.iloc[0]

def get_predict(df):
  

def stock():
  while True:
    code = input("코드 입력 : ")
    if len(code) == 6:
      print("종목 코드:", code)
      normalized_df = get_df(code)
       
    else:
      print("잘못된 입력") 

if __name__ == "__main__":
  stock()