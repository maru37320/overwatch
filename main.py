import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="OWTICS S21 MID", page_icon="🔥", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@500;700&display=swap');
    
    .stApp { background-color: #1b1c23; color: #f0edee; font-family: 'Malgun Gothic', sans-serif;}
    
    .ow-header {
        font-family: 'Teko', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        font-style: italic;
        color: #f99e1a;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* 포지션별 1티어 강조 카드 */
    .tier-card {
        padding: 20px;
        border-radius: 8px;
        background-color: #2b2d37;
        border-left: 6px solid;
    }
    .tank-card { border-left-color: #4EA8DE; }
    .dmg-card { border-left-color: #F4556C; }
    .sup-card { border-left-color: #38E09E; }
    
    .tier-title { font-family: 'Teko', sans-serif; font-size: 1.8rem; font-style: italic; color: white; margin: 0; line-height: 1.2;}
    .tier-stat { font-size: 1.1rem; font-weight: bold; color: #f99e1a; margin-top: 5px;}
</style>
""", unsafe_allow_html=True)

# 🌅 메인 배너 이미지 소환 (전체 영웅 공식 초상화 배너)
st.image("https://raw.githubusercontent.com/username/OWTICS_Dashboard/main/assets/main_banner_official.png", caption="OWTICS.GG SEASON 21 MID DASHBOARD (OFFICIAL PORTRAITS)", use_container_width=True)

st.markdown('<div class="ow-header">S21 MID META DASHBOARD</div>', unsafe_allow_html=True)

# 데이터 로드 (50명 전체 데이터 - 동일)
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

# --- 👑 1티어 공식 얼굴 카드 소환 ---
with c1:
    # 예시: 공식 시그마 초상화 이미지 (sigma_official.png)
    st.image("https://raw.githubusercontent.com/username/OWTICS_Dashboard/main/assets/sigma_official.png", width=80) 
    st.markdown(f"""<div class="tier-card tank-card"><p class="tier-title">🛡️ TANK: {tank_top['영웅']}</p><p class="tier-stat">픽률 {tank_top['픽률(%)']}% | 승률 {tank_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)
with c2:
    # 예시: 공식 캐서디 초상화 이미지 (cassidy_official.png)
    st.image("https://raw.githubusercontent.com/username/OWTICS_Dashboard/main/assets/cassidy_official.png", width=80)
    st.markdown(f"""<div class="tier-card dmg-card"><p class="tier-title">⚔️ DAMAGE: {dmg_top['영웅']}</p><p class="tier-stat">픽률 {dmg_top['픽률(%)']}% | 승률 {dmg_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)
with c3:
    # 예시: 공식 아나 초상화 이미지 (ana_official.png)
    st.image("https://raw.githubusercontent.com/username/OWTICS_Dashboard/main/assets/ana_official.png", width=80)
    st.markdown(f"""<div class="tier-card sup-card"><p class="tier-title">💉 SUPPORT: {sup_top['영웅']}</p><p class="tier-stat">픽률 {sup_top['픽률(%)']}% | 승률 {sup_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 🔥 리더보드 그래프 (글꼴 적용) ---
colA, colB = st.columns(2)

with colA:
    st.markdown("### 🔥 OVERALL TOP 5 PICK RATE")
    top_picks = df.sort_values('픽률(%)', ascending=False).head(5)
    fig_pick = px.bar(top_picks, x='픽률(%)', y='영웅', orientation='h', text='픽률(%)', color='포지션', color_discrete_map={'탱커':'#4EA8DE', '딜러':'#F4556C', '힐러':'#38E09E'})
    fig_pick.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=16))
    fig_pick.update_traces(textposition='outside')
    st.plotly_chart(fig_pick, use_container_width=True)

with colB:
    st.markdown("### 🏆 OVERALL TOP 5 WIN RATE")
    top_wins = df.sort_values('승률(%)', ascending=False).head(5)
    fig_win = px.bar(top_wins, x='승률(%)', y='영웅', orientation='h', text='승률(%)', color='포지션', color_discrete_map={'탱커':'#4EA8DE', '딜러':'#F4556C', '힐러':'#38E09E'})
    fig_win.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white', family="Teko, sans-serif", size=16))
    fig_win.update_traces(textposition='outside')
    st.plotly_chart(fig_win, use_container_width=True)

st.divider()

# --- 📋 전체 데이터 표 (동일) ---
st.markdown("### 📋 FULL HERO LEADERBOARD")
st.dataframe(df[['영웅', '포지션', '세부역할', '픽률(%)', '승률(%)']], use_container_width=True, hide_index=True, column_config={"픽률(%)": st.column_config.ProgressColumn("픽률(%)", format="%f%%", min_value=0, max_value=50), "승률(%)": st.column_config.NumberColumn("승률(%)", format="%f%%")})
