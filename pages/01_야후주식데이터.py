import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# 시가총액 상위 10개 기업
top_10_companies = ["MSFT", "NVDA", "AAPL", "AMZN", "GOOG", "META", "TSLA", "BRK-B", "AVGO", "TSM"]

# 데이터 가져오기
st.title("글로벌 시가총액 Top 10 기업의 최근 1년 주가 변화")

start_date = "2024-05-20"
end_date = "2025-05-20"

fig = go.Figure()

for company in top_10_companies:
    stock_data = yf.download(company, start=start_date, end=end_date)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Close"], mode="lines", name=company))

fig.update_layout(title="최근 1년간 글로벌 시가총액 Top 10 기업 주가 변화",
                  xaxis_title="날짜",
                  yaxis_title="주가 ($)",
                  template="plotly_white")

st.plotly_chart(fig)

