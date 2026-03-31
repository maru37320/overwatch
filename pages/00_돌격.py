import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="TANK STATS", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@500;700&display=swap');
    .stApp { background-color: #1b1c23; color: #f0edee; font-family: 'Malgun Gothic', sans-serif;}
    h1, h2, h3 { font-family: 'Teko', sans-serif !important; font-style: italic; color: #4EA8DE !important; }
</style>
""", unsafe_allow_html=True)

# 🌅 탱커 공식 얼굴 배너 이미지 소환 (탱커 공식 초상화 배너)
st.image("https://raw.githubusercontent.com/username/OWTICS_Dashboard/main/assets/tank_header_official.png", caption="TANK HEROES METRICS (OFFICIAL PORTRAITS)", use_container_width=True)

st.title("🛡️ TANK HERO METRICS")

if os.path.exists('owtics_s21_exact_data.csv'):
    df = pd.read_csv('owtics_s21_exact_data.csv')
else:
    st.error("app.py를 먼저 실행해 주세요.")
    st.stop()

tank_df = df[df['포지션'] == '탱커']

col1, col2 = st.columns(2)

with col1:
    st.subheader("PICK RATE (%)")
    fig_pick = px.bar(tank_df.sort_values('픽률(%)', ascending=False), x='영웅', y='픽률(%)', text_auto='.1f', color='세부역할', color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_pick.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=16))
    st.plotly_chart(fig_pick, use_container_width=True)

with col2:
    st.subheader("WIN RATE (%)")
    fig_win = px.bar(tank_df.sort_values('승률(%)', ascending=False), x='영웅', y='승률(%)', text_auto='.1f', color='세부역할', color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_win.add_hline(y=50, line_dash="dash", line_color="red")
    fig_win.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=16), yaxis=dict(range=[35, 60]))
    st.plotly_chart(fig_win, use_container_width=True)
