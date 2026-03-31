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
    .hero-card { background: #2b2d37; padding: 15px; border-radius: 10px; text-align: center; border-bottom: 4px solid #4EA8DE; }
    .hero-card img { border-radius: 50%; width: 80px; height: 80px; object-fit: cover; border: 2px solid #4EA8DE; }
    .dark-table { width: 100%; border-collapse: collapse; font-family: 'Malgun Gothic', sans-serif; color: white; background-color: #1b1c23; text-align: center; margin-top: 10px; }
    .dark-table th { background-color: #4EA8DE; color: #1b1c23; padding: 10px; font-family: 'Teko', sans-serif; font-size: 1.5rem; }
    .dark-table td { padding: 8px; border-bottom: 1px solid #333; }
    .hero-img { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ TANK HERO METRICS")

if os.path.exists('owtics_s21_exact_data.csv'):
    df = pd.read_csv('owtics_s21_exact_data.csv')
else:
    st.error("메인 페이지를 먼저 실행해서 데이터를 로드해주세요!")
    st.stop()

tank_df = df[df['포지션'] == '탱커'].sort_values('픽률(%)', ascending=False)

st.subheader("🏆 TOP 3 TANKS")
cols = st.columns(3)
for i in range(3):
    hero = tank_df.iloc[i]
    with cols[i]:
        st.markdown(f"""<div class="hero-card"><img src="{hero['초상화']}"><h3 style="margin:5px 0;">{i+1}. {hero['영웅']}</h3><p style="margin:0; color:#ccc;">픽률 {hero['픽률(%)']}% | 승률 {hero['승률(%)']}%</p></div>""", unsafe_allow_html=True)

st.divider()

# --- 🎯 얼굴 박힌 스캐터 플롯 ---
st.subheader("🎯 META ANALYSIS (PICK RATE vs WIN RATE)")
# 기본 스캐터 플롯 생성 (점은 투명하게, 텍스트는 아래로)
fig_scatter = px.scatter(tank_df, x='픽률(%)', y='승률(%)', text='영웅', hover_data=['세부역할'])
fig_scatter.update_traces(marker=dict(opacity=0), textposition='bottom center', textfont=dict(color='white'))

# 좌표에 영웅 초상화 이미지 추가
for _, row in tank_df.iterrows():
    fig_scatter.add_layout_image(
        dict(
            source=row['초상화'], x=row['픽률(%)'], y=row['승률(%)'],
            xref="x", yref="y",
            sizex=1.5, sizey=1.5, # 탱커 축 비율에 맞춘 이미지 사이즈
            xanchor="center", yanchor="middle",
            sizing="contain", layer="above"
        )
    )

fig_scatter.add_hline(y=50, line_dash="dash", line_color="red", annotation_text="승률 50% 기준선", annotation_font_color="white")
# 얼굴이 안 잘리게 여백 추가
fig_scatter.update_xaxes(range=[tank_df['픽률(%)'].min() - 2, tank_df['픽률(%)'].max() + 2])
fig_scatter.update_yaxes(range=[tank_df['승률(%)'].min() - 2, tank_df['승률(%)'].max() + 3])
fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(family="Teko, sans-serif", size=14), height=600)

st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("📋 TANK LEADERBOARD")
html_table = "<table class='dark-table'><tr><th>FACE</th><th>영웅</th><th>세부역할</th><th>픽률(%)</th><th>승률(%)</th></tr>"
for _, row in tank_df.iterrows():
    html_table += f"<tr><td><img src='{row['초상화']}' class='hero-img'></td><td>{row['영웅']}</td><td>{row['세부역할']}</td><td>{row['픽률(%)']}</td><td>{row['승률(%)']}</td></tr>"
html_table += "</table>"
st.markdown(html_table, unsafe_allow_html=True)
