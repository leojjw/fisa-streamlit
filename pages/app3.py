import yfinance as yf
import streamlit as st

data = yf.download(['AAPL'],start = '2019-01-01')

st.write(data)