import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 샘플 데이터 생성
data = {
    "Age Group": ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"],
    "Male": [-500, -600, -700, -800, -900, -950, -900, -850, -800, -750, -700, -650, -600, -550, -500, -450, -400],
    "Female": [480, 580, 680, 780, 880, 930, 880, 830, 780, 730, 680, 630, 580, 530, 480, 430, 380]
}

df = pd.DataFrame(data)

# 그래프 생성
fig = go.Figure()
fig.add_trace(go.Bar(y=df["Age Group"], x=df["Male"], orientation='h', name="Male", marker_color='blue'))
fig.add_trace(go.Bar(y=df["Age Group"], x=df["Female"], orientation='h', name="Female", marker_color='red'))

fig.update_layout(
    title="인구 구조 피라미드",
    barmode="relative",
    bargap=0.1,
    xaxis=dict(title="Population", tickvals=[-1000, -500, 0, 500, 1000], ticktext=["1000", "500", "0", "500", "1000"]),
    yaxis=dict(title="Age Group"),
    template="plotly_white"
)

# Streamlit에서 그래프 표시
st.title("인구 구조 피라미드")
st.plotly_chart(fig)
