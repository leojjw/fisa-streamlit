import mojito
import pprint
import streamlit as st

f = open("C:/Users/leojj/auto_trading/koreainvestment.key")

mode = 0 # REAL = 0, MOCK = 1

lines = f.readlines()

if (mode == 0):
    key = lines[1].strip()
    secret = lines[2].strip()
    acc_no = lines[3].strip()
else:
    key = lines[4].strip()
    secret = lines[5].strip()
    acc_no = lines[6].strip()


f.close()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no,
    mock = False if mode == 0 else True
)

# 차트를 구한다.
# macd를 구한다.
# '그 선'을 구한다.

resp = broker.fetch_ohlcv(
    symbol="005930",
    timeframe='D',
    adj_price=True
)

pprint.pprint(len(resp['output2']))

st.write(len(resp['output2']))
