import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import requests

st.set_page_config(page_title="OWTICS S21 MID", page_icon="🔥", layout="wide")

# --- 🕵️‍♂️ "나 봇 아니야 크롬이야" 이미지 자동 다운로드 함수 ---
def sneak_download_image(url, save_path):
    if not os.path.exists("assets"):
        os.makedirs("assets")
    if not os.path.exists(save_path):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Referer": "https://www.google.com/"
        }
        try:
            response = requests.get(url, headers=headers, stream=True)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
        except Exception as e:
            pass

# 필수 이미지 자동 다운로드 실행 (오버워치 위키/공식 이미지 URL 예시)
sneak_download_image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Overwatch_circle_logo.svg/500px-Overwatch_circle_logo.svg.png", "assets/main_banner.png")
sneak_download_image("https://static.wikia.nocookie.net/overwatch_gamepedia/images/1/14/Sigma_portrait.png", "assets/sigma.png")
sneak_download_image("https://static.wikia.nocookie.net/overwatch_gamepedia/images/a/ab/Cassidy_portrait.png", "assets/cassidy.png")
sneak_download_image("https://static.wikia.nocookie.net/overwatch_gamepedia/images/2/29/Ana_portrait.png", "assets/ana.png")

# --- CSS 스타일링 ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@500;700&display=swap');
    .stApp { background-color: #1b1c23; color: #f0edee; }
    .ow-header { font-family: 'Teko', sans-serif; font-size: 4rem; font-weight: 700; font-style: italic; color: #f99e1a; text-shadow: 2px 2px 10px rgba(249,158,26,0.5); text-transform: uppercase; }
    .tier-card { padding: 20px; border-radius: 12px; background: linear-gradient(145deg, #2b2d37, #1e1f26); box-shadow: 0 4px 15px rgba(0,0,0,0.5); border-left: 6px solid; transition: transform 0.2s; }
    .tier-card:hover { transform: scale(1.02); }
    .tank-card { border-left-color: #4EA8DE; box-shadow: 0 0 15px rgba(78,168,222,0.3); }
    .dmg-card { border-left-color: #F4556C; box-shadow: 0 0 15px rgba(244,85,108,0.3); }
    .sup-card { border-left-color: #38E09E; box-shadow: 0 0 15px rgba(56,224,158,0.3); }
    .tier-title { font-family: 'Teko', sans-serif; font-size: 2.2rem; font-style: italic; color: white; margin: 0; line-height: 1.1;}
    .tier-stat { font-size: 1.2rem; font-weight: bold; color: #f99e1a; margin-top: 8px;}
</style>
""", unsafe_allow_html=True)

st.image("assets/main_banner.png" if os.path.exists("assets/main_banner.png") else "https://placehold.co/1200x300/2b2d37/f99e1a/png?text=OVERWATCH+META", width=150)
st.markdown('<div class="ow-header">S21 MID META DASHBOARD</div>', unsafe_allow_html=True)

# 데이터 생성
data = {
    '영웅': ['시그마', '도미나', '윈스턴', '오리사', '디바', '자리야', '라인하르트', '둠피스트', '라마트라', '로드호그', '레킹볼', '마우가', '정커퀸', '해저드', '캐서디', '엠레', 'Soldier: 76', '소전', '겐지', '애쉬', '안란', '리퍼', '바스티온', '트레이서', '한조', '정크랫', '메이', '파라', '에코', '프레야', '위도우메이커', '벤데타', '시메트라', '벤처', '솜브라', '토르비욘', '아나', '바티스트', '브리기테', '일리아리', '제트팩 캣', '주노', '키리코', '라이프위버', '루시우', '메르시', '미즈키', '모이라', '우양', '젠야타'],
    '포지션': ['탱커']*14 + ['딜러']*22 + ['힐러']*14,
    '세부역할': ['강건한 자', '강건한 자', '개시자', '투사', '개시자', '투사', '강건한 자', '개시자', '강건한 자', '투사', '개시자', '투사', '강건한 자', '강건한 자', '명사수', '전문가', '전문가', '명사수', '측면 공격가', '명사수', '측면 공격가', '측면 공격가', '전문가', '측면 공격가', '명사수', '전문가', '전문가', '수색가', '수색가', '수색가', '명사수', '측면 공격가', '전문가', '측면 공격가', '수색가', '전문가', '전술가', '전술가', '생존 전문가', '생존 전문가', '전술가', '생존 전문가', '의무병', '의무병', '전술가', '의무병', '생존 전문가', '의무병', '생존 전문가', '전술가'],
    '픽률(%)': [14.1, 11.4, 10.8, 10.1, 9.0, 8.7, 7.9, 6.8, 5.8, 4.3, 3.4, 3.1, 2.8, 1.8, 21.9, 18.2, 17.9, 15.0, 13.8, 13.4, 12.4, 11.8, 9.2, 8.4, 7.1, 6.3, 5.9, 5.6, 5.3, 4.4, 4.2, 4.2, 4.1, 4.0, 3.8, 3.3, 47.2, 7.7, 3.5, 12.6, 5.5, 10.8, 33.2, 3.9, 5.6, 8.9, 21.9, 15.7, 12.7, 10.8],
    '승률(%)': [53.2, 53.8, 52.3, 45.2, 49.5, 48.1, 49.2, 52.0, 46.4, 40.9, 50.7, 46.3, 51.2, 47.0, 46.9, 49.7, 48.5, 45.8, 51.5, 51.0, 50.8, 51.1, 47.4, 50.2, 49.8, 48.2, 49.9, 52.3, 51.7, 47.2, 50.0, 53.7, 53.8, 51.8, 49.6, 49.2, 49.6, 45.3, 46.5, 54.4, 51.9, 49.9, 47.1, 43.6, 47.9, 47.0, 52.7, 47.8, 52.2, 52.3]
}
df = pd.DataFrame(data)
df.to_csv('owtics_s21_exact_data.csv', index=False)

st.markdown("### 👑 CURRENT 1 TIER HEROES")
c1, c2, c3 = st.columns(3)
tank_top = df[df['포지션']=='탱커'].sort_values('픽률(%)', ascending=False).iloc[0]
dmg_top = df[df['포지션']=='딜러'].sort_values('픽률(%)', ascending=False).iloc[0]
sup_top = df[df['포지션']=='힐러'].sort_values('픽률(%)', ascending=False).iloc[0]

with c1:
    img_path = "assets/sigma.png" if os.path.exists("assets/sigma.png") else "https://placehold.co/100/2b2d37/4EA8DE/png?text=TANK"
    st.markdown(f"""<div class="tier-card tank-card"><img src="{img_path}" width="70" style="border-radius:50%; margin-bottom:10px;"><p class="tier-title">{tank_top['영웅']}</p><p class="tier-stat">픽률 {tank_top['픽률(%)']}% | 승률 {tank_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)
with c2:
    img_path = "assets/cassidy.png" if os.path.exists("assets/cassidy.png") else "https://placehold.co/100/2b2d37/F4556C/png?text=DMG"
    st.markdown(f"""<div class="tier-card dmg-card"><img src="{img_path}" width="70" style="border-radius:50%; margin-bottom:10px;"><p class="tier-title">{dmg_top['영웅']}</p><p class="tier-stat">픽률 {dmg_top['픽률(%)']}% | 승률 {dmg_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)
with c3:
    img_path = "assets/ana.png" if os.path.exists("assets/ana.png") else "https://placehold.co/100/2b2d37/38E09E/png?text=SUP"
    st.markdown(f"""<div class="tier-card sup-card"><img src="{img_path}" width="70" style="border-radius:50%; margin-bottom:10px;"><p class="tier-title">{sup_top['영웅']}</p><p class="tier-stat">픽률 {sup_top['픽률(%)']}% | 승률 {sup_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 화려하게 바뀐 풀 히어로 리더보드 (Plotly Table 활용)
st.markdown("### 📋 FULL HERO LEADERBOARD")
fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='#f99e1a',
                font=dict(color='black', family="Teko, sans-serif", size=18),
                align='center'),
    cells=dict(values=[df['영웅'], df['포지션'], df['세부역할'], df['픽률(%)'], df['승률(%)']],
               fill_color='#2b2d37',
               font=dict(color='white', size=14),
               align='center',
               height=30))
])
fig_table.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_table, use_container_width=True)
