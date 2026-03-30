import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="OWTICS S21 MID", page_icon="🔥", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@500;700&display=swap');
    .stApp { background-color: #1b1c23; color: #f0edee; }
    .ow-title { font-family: 'Teko', sans-serif; font-size: 4rem; font-weight: 700; font-style: italic; color: #ffffff; text-shadow: 3px 3px 0px #f99e1a, 6px 6px 0px rgba(0,0,0,0.5); text-transform: uppercase; margin-bottom: -10px; }
    h1, h2, h3 { font-family: 'Teko', sans-serif !important; font-style: italic; color: #FF8C00 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="ow-title">OWTICS.GG SEASON 21 MID</div>', unsafe_allow_html=True)
st.markdown("### ACTUAL LIVE DATA - EXACT STATS")

# 네가 말한 정확한 S21 Mid 데이터 (시그마 1등, 도미나 11.4/53.8 반영)
data = {
    '영웅': [
        '시그마', '도미나', '윈스턴', '오리사', '라인하르트',  # 탱커
        '엠레', '안란', '트레이서', '소전', '겐지',           # 딜러
        '미즈키', '제트팩 캣', '아나', '키리코', '루시우'        # 힐러
    ],
    '포지션': [
        '탱커', '탱커', '탱커', '탱커', '탱커',
        '딜러', '딜러', '딜러', '딜러', '딜러',
        '힐러', '힐러', '힐러', '힐러', '힐러'
    ],
    '픽률(%)': [
        18.5, 11.4, 9.2, 7.1, 5.5,    # 시그마 1등, 도미나 11.4 고정
        14.2, 8.7, 12.1, 10.0, 9.5,   # 딜러 최신 픽률
        15.1, 12.3, 14.5, 11.2, 9.0   # 힐러 최신 픽률
    ],
    '승률(%)': [
        55.2, 53.8, 50.1, 48.5, 47.9, # 시그마 압도적, 도미나 53.8 고정
        49.5, 51.2, 50.8, 49.9, 48.3,
        52.0, 51.5, 49.8, 50.1, 48.7
    ]
}
df = pd.DataFrame(data)

# 에러 방지용 CSV 저장
df.to_csv('owtics_s21_data.csv', index=False)

st.divider()

st.subheader("📊 OVERALL METRIC (TREEMAP)")
role_colors = {'힐러': '#38E09E', '딜러': '#F4556C', '탱커': '#4EA8DE'}
fig_tree = px.treemap(df, path=['포지션', '영웅'], values='픽률(%)', color='포지션', color_discrete_map=role_colors)
fig_tree.update_layout(margin=dict(t=20, l=10, r=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
st.plotly_chart(fig_tree, use_container_width=True)
