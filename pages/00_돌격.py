import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="TANK STATS", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@500;700&display=swap');
    .stApp { background-color: #1b1c23; color: #f0edee; }
    h1, h2, h3 { font-family: 'Teko', sans-serif !important; font-style: italic; color: #4EA8DE !important; text-shadow: 0 0 10px rgba(78,168,222,0.5); }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ TANK HERO METRICS")

if os.path.exists('owtics_s21_exact_data.csv'):
    df = pd.read_csv('owtics_s21_exact_data.csv')
else:
    st.stop()

tank_df = df[df['포지션'] == '탱커']

# 🌟 신규 화려한 스캐터 플롯 (OP 영웅 찾기)
st.subheader("🎯 META ANALYSIS (PICK RATE vs WIN RATE)")
fig_scatter = px.scatter(tank_df, x='픽률(%)', y='승률(%)', text='영웅', size='픽률(%)', color='세부역할',
                         color_discrete_sequence=px.colors.sequential.Blues_r)
fig_scatter.update_traces(textposition='top center', marker=dict(line=dict(width=2, color='white')))
fig_scatter.add_hline(y=50, line_dash="dash", line_color="red", annotation_text="승률 50% 기준선")
fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=14), height=500)
st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("PICK RATE (%)")
    fig_pick = px.bar(tank_df.sort_values('픽률(%)', ascending=False), x='영웅', y='픽률(%)', text_auto='.1f', color='세부역할', color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_pick.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=14))
    st.plotly_chart(fig_pick, use_container_width=True)
with col2:
    st.subheader("WIN RATE (%)")
    fig_win = px.bar(tank_df.sort_values('승률(%)', ascending=False), x='영웅', y='승률(%)', text_auto='.1f', color='세부역할', color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_win.add_hline(y=50, line_dash="dash", line_color="red")
    fig_win.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=14), yaxis=dict(range=[35, 60]))
    st.plotly_chart(fig_win, use_container_width=True)
