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
st.markdown("### EXACT LIVE HERO STATS")

# 유저가 직접 떠먹여준 완벽한 S21 Mid 데이터 (영웅 50명 전체)
data = {
    '영웅': [
        # 탱커 (14)
        '시그마', '도미나', '윈스턴', '오리사', '디바', '자리야', '라인하르트', '둠피스트', '라마트라', '로드호그', '레킹볼', '마우가', '정커퀸', '해저드',
        # 딜러 (22)
        '캐서디', '엠레', 'Soldier: 76', '소전', '겐지', '애쉬', '안란', '리퍼', '바스티온', '트레이서', '한조', '정크랫', '메이', '파라', '에코', '프레야', '위도우메이커', '벤데타', '시메트라', '벤처', '솜브라', '토르비욘',
        # 힐러 (14)
        '아나', '바티스트', '브리기테', '일리아리', '제트팩 캣', '주노', '키리코', '라이프위버', '루시우', '메르시', '미즈키', '모이라', '우양', '젠야타'
    ],
    '포지션': [
        '탱커']*14 + ['딜러']*22 + ['힐러']*14,
    '세부역할': [
        # 탱커 세부
        '강건한 자', '강건한 자', '개시자', '투사', '개시자', '투사', '강건한 자', '개시자', '강건한 자', '투사', '개시자', '투사', '강건한 자', '강건한 자',
        # 딜러 세부
        '명사수', '전문가', '전문가', '명사수', '측면 공격가', '명사수', '측면 공격가', '측면 공격가', '전문가', '측면 공격가', '명사수', '전문가', '전문가', '수색가', '수색가', '수색가', '명사수', '측면 공격가', '전문가', '측면 공격가', '수색가', '전문가',
        # 힐러 세부
        '전술가', '전술가', '생존 전문가', '생존 전문가', '전술가', '생존 전문가', '의무병', '의무병', '전술가', '의무병', '생존 전문가', '의무병', '생존 전문가', '전술가'
    ],
    '픽률(%)': [
        14.1, 11.4, 10.8, 10.1, 9.0, 8.7, 7.9, 6.8, 5.8, 4.3, 3.4, 3.1, 2.8, 1.8, # 탱커
        21.9, 18.2, 17.9, 15.0, 13.8, 13.4, 12.4, 11.8, 9.2, 8.4, 7.1, 6.3, 5.9, 5.6, 5.3, 4.4, 4.2, 4.2, 4.1, 4.0, 3.8, 3.3, # 딜러
        47.2, 7.7, 3.5, 12.6, 5.5, 10.8, 33.2, 3.9, 5.6, 8.9, 21.9, 15.7, 12.7, 10.8 # 힐러
    ],
    '승률(%)': [
        53.2, 53.8, 52.3, 45.2, 49.5, 48.1, 49.2, 52.0, 46.4, 40.9, 50.7, 46.3, 51.2, 47.0, # 탱커
        46.9, 49.7, 48.5, 45.8, 51.5, 51.0, 50.8, 51.1, 47.4, 50.2, 49.8, 48.2, 49.9, 52.3, 51.7, 47.2, 50.0, 53.7, 53.8, 51.8, 49.6, 49.2, # 딜러
        49.6, 45.3, 46.5, 54.4, 51.9, 49.9, 47.1, 43.6, 47.9, 47.0, 52.7, 47.8, 52.2, 52.3 # 힐러
    ]
}
df = pd.DataFrame(data)
df.to_csv('owtics_s21_exact_data.csv', index=False)

st.divider()

st.subheader("📊 OVERALL METRIC (TREEMAP)")
role_colors = {'힐러': '#38E09E', '딜러': '#F4556C', '탱커': '#4EA8DE'}
fig_tree = px.treemap(
    df, path=['포지션', '세부역할', '영웅'], values='픽률(%)', 
    color='포지션', color_discrete_map=role_colors,
    hover_data=['승률(%)']
)
fig_tree.update_layout(margin=dict(t=20, l=10, r=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
st.plotly_chart(fig_tree, use_container_width=True)

st.success("데이터 로드 완료! 좌측 사이드바에서 세부 포지션 페이지를 확인하세요.")
