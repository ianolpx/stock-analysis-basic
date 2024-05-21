import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

code = input("코드 입력")

if code == "005930":
  print("Samsung Electronics")
  yf.pdr_override()
  df1 = pdr.get_data_yahoo("005930.KS", "2024-04-01", "2024-05-01")
  print(df1)
  code1 = input("주식 종목 코드를 입력하세요 (예: 005930): ")
  start_date = input("시작 날짜를 입력하세요 (예: 2024-04-01): ")
  end_date = input("종료 날짜를 입력하세요 (예: 2024-04-30): ")
  dfa = pdr.get_data_yahoo("005930.KS", start=start_date, end=end_date)
  plt.figure(figsize=(14, 6))
  plt.plot(dfa['Close'], label='종가')
  plt.title(f'{code1} 주식 가격')
  plt.xlabel('날짜')
  plt.ylabel('가격')
  plt.legend()
  plt.grid()
  plt.show()

elif code == "068270":
  print("Celltrion")
  yf.pdr_override()
  df2 = pdr.get_data_yahoo("068270.KS", "2024-04-01", "2024-05-01")
  print(df2)
  code2 = input("주식 종목 코드를 입력하세요 (예: 068270): ")
  start_date = input("시작 날짜를 입력하세요 (예: 2024-04-01): ")
  end_date = input("종료 날짜를 입력하세요 (예: 2024-04-30): ")
  dfa = pdr.get_data_yahoo("068270.KS", start=start_date, end=end_date)
  plt.figure(figsize=(14, 6))
  plt.plot(dfa['Close'], label='종가')
  plt.title(f'{code2} 주식 가격')
  plt.xlabel('날짜')
  plt.ylabel('가격')
  plt.legend()
  plt.grid()
  plt.show()
  
elif code == "011070":
  print("LG innotec")
  yf.pdr_override()
  df3 = pdr.get_data_yahoo("011070.KS", "2024-04-01", "2024-05-01")
  print(df3)
  code3 = input("주식 종목 코드를 입력하세요 (예: 011070): ")
  start_date = input("시작 날짜를 입력하세요 (예: 2024-04-01): ")
  end_date = input("종료 날짜를 입력하세요 (예: 2024-04-30): ")
  dfa = pdr.get_data_yahoo("011070.KS", start=start_date, end=end_date)
  plt.figure(figsize=(14, 6))
  plt.plot(dfa['Close'], label='종가')
  plt.title(f'{code3} 주식 가격')
  plt.xlabel('날짜')
  plt.ylabel('가격')
  plt.legend()
  plt.grid()
  plt.show()
  
else:
  print("등록되지 않은 코드")

if code == "005930p":
  print("Yield")
  yf.pdr_override()
  df1 = pdr.get_data_yahoo("005930.KS", "2024-04-01", "2024-05-01")
  dfs = df1.iloc[:,0:1]
  dfs1 = dfs.rename(columns={'Open':'Price'})
  dfs1["Y_Price"] = dfs1.shift(1)
  dfs1["M.Price"] = dfs1.Price.sub(dfs1.Y_Price)
  dfs1["Yield"] = (dfs1.Price.div(dfs1.Y_Price) - 1) * 100
  dfs1
  a = input()
  if a in dfs1.index:
        print(dfs1.loc[a])
  else:
      print("해당 날짜의 데이터가 없습니다.")

elif code == "068270p":
  print("Yield")
  yf.pdr_override()
  df2 = pdr.get_data_yahoo("068270.KS", "2024-04-01", "2024-05-01")
  dfc = df2.iloc[:,0:1]
  dfc1 = dfc.rename(columns={'Open':'Price'})
  dfc1["Y_Price"] = dfc1.shift(1)
  dfc1["M.Price"] = dfc1.Price.sub(dfc1.Y_Price)
  dfc1["Yield"] = (dfc1.Price.div(dfc1.Y_Price) - 1) * 100
  dfc1
  a = input()
  if a in dfc1.index:
        print(dfc1.loc[a])
  else:
      print("해당 날짜의 데이터가 없습니다.")

elif code == "011070p":
  print("Yield")
  yf.pdr_override()
  df3 = pdr.get_data_yahoo("011070.KS", "2024-04-01", "2024-05-01")
  dfl = df3.iloc[:,0:1]
  dfl1 = dfl.rename(columns={'Open':'Price'})
  dfl1["Y_Price"] = dfl1.shift(1)
  dfl1["M.Price"] = dfl1.Price.sub(dfl1.Y_Price)
  dfl1["Yield"] = (dfl1.Price.div(dfl1.Y_Price) - 1) * 100
  dfl1
  a = input()
  if a in dfl1.index:
        print(dfl1.loc[a])
  else:
      print("해당 날짜의 데이터가 없습니다.")

else:
  print("np")