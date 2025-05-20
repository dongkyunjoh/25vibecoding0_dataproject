import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# 시가총액 상위 10개 기업
top_10_companies = ["MSFT", "NVDA", "AAPL", "AMZN", "GOOG", "META", "TSLA", "BRK-B", "AVGO", "TSM"]

# 데이터 가져오기
st.title("📈 글로벌 시가총액 Top 10 기업의 최근 1년 주가 변화")

start_date = "2024-05-20"
end_date = "2025-05-20"

fig = go.Figure()

for company in top_10_companies:
    stock_data = yf.download(company, start=start_date, end=end_date)

    # 데이터가 정상적으로 가져왔는지 확인
    if stock_data.empty:
        st.warning(f"{company}의 데이터를 가져오지 못했습니다.")
        continue

    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Close"], 
                             mode="lines", name=company,
                             line=dict(width=2)))  # 선 두께 증가

# X축 날짜 슬라이더 추가
fig.update_xaxes(rangeslider_visible=True)

# 로그 스케일 적용 (주가 차이가 큰 경우 대비)
fig.update_yaxes(type="log")

fig.update_layout(title="최근 1년간 글로벌 시가총액 Top 10 기업 주가 변화",
                  xaxis_title="날짜",
                  yaxis_title="주가 ($)",
                  template="plotly_white")

# Streamlit에서 그래프 표시
st.plotly_chart(fig)
