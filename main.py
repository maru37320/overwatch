import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="OWTICS S21 MID", page_icon="🔥", layout="wide")

@st.cache_data
def fetch_official_hero_portraits():
    url = "https://overfast-api.tekrop.fr/heroes?locale=ko-kr"
    img_dict = {}
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                name = item['name']
                if name == 'D.Va': name = '디바'
                if name == '솔저: 76': name = 'Soldier: 76'
                img_dict[name] = item['portrait']
    except Exception as e:
        pass
    return img_dict

hero_images = fetch_official_hero_portraits()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@400;500;700&display=swap');
    .stApp { background-color: #1b1c23; color: #f0edee; }
    .ow-header { font-family: 'Teko', sans-serif; font-size: 4rem; font-weight: 700; font-style: italic; color: #f99e1a; text-shadow: 2px 2px 10px rgba(249,158,26,0.5); text-transform: uppercase; }
    .tier-card { padding: 20px; border-radius: 12px; background: linear-gradient(145deg, #2b2d37, #1e1f26); box-shadow: 0 4px 15px rgba(0,0,0,0.5); border-left: 6px solid; transition: transform 0.2s; text-align: center;}
    .tier-card:hover { transform: scale(1.02); }
    .tank-card { border-left-color: #4EA8DE; box-shadow: 0 0 15px rgba(78,168,222,0.3); }
    .dmg-card { border-left-color: #F4556C; box-shadow: 0 0 15px rgba(244,85,108,0.3); }
    .sup-card { border-left-color: #38E09E; box-shadow: 0 0 15px rgba(56,224,158,0.3); }
    .tier-title { font-family: 'Teko', sans-serif; font-size: 2.2rem; font-style: italic; color: white; margin: 10px 0 0 0; line-height: 1.1;}
    .tier-stat { font-family: 'Teko', sans-serif; font-size: 1.4rem; font-weight: 500; color: #f99e1a; margin-top: 5px; letter-spacing: 1px;}
    
    /* 🔥 폰트 통일된 커스텀 다크모드 테이블 CSS */
    .dark-table { width: 100%; border-collapse: collapse; font-family: 'Teko', sans-serif; font-size: 1.4rem; letter-spacing: 1px; color: white; background-color: #1b1c23; text-align: center; margin-top: 10px; }
    .dark-table th { background-color: #f99e1a; color: #1b1c23; padding: 12px; font-weight: 700; font-size: 1.6rem; letter-spacing: 1px; }
    .dark-table td { padding: 8px; border-bottom: 1px solid #333; vertical-align: middle; font-weight: 400; }
    .dark-table tr:hover { background-color: #2b2d37; }
    .hero-img { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #555; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="ow-header">S21 MID META DASHBOARD</div>', unsafe_allow_html=True)

data = {
    '영웅': ['시그마', '도미나', '윈스턴', '오리사', '디바', '자리야', '라인하르트', '둠피스트', '라마트라', '로드호그', '레킹볼', '마우가', '정커퀸', '해저드', '캐서디', '엠레', 'Soldier: 76', '소전', '겐지', '애쉬', '안란', '리퍼', '바스티온', '트레이서', '한조', '정크랫', '메이', '파라', '에코', '프레야', '위도우메이커', '벤데타', '시메트라', '벤처', '솜브라', '토르비욘', '아나', '바티스트', '브리기테', '일리아리', '제트팩 캣', '주노', '키리코', '라이프위버', '루시우', '메르시', '미즈키', '모이라', '우양', '젠야타'],
    '포지션': ['탱커']*14 + ['딜러']*22 + ['힐러']*14,
    '세부역할': ['강건한 자', '강건한 자', '개시자', '투사', '개시자', '투사', '강건한 자', '개시자', '강건한 자', '투사', '개시자', '투사', '강건한 자', '강건한 자', '명사수', '전문가', '전문가', '명사수', '측면 공격가', '명사수', '측면 공격가', '측면 공격가', '전문가', '측면 공격가', '명사수', '전문가', '전문가', '수색가', '수색가', '수색가', '명사수', '측면 공격가', '전문가', '측면 공격가', '수색가', '전문가', '전술가', '전술가', '생존 전문가', '생존 전문가', '전술가', '생존 전문가', '의무병', '의무병', '전술가', '의무병', '생존 전문가', '의무병', '생존 전문가', '전술가'],
    '픽률(%)': [14.1, 11.4, 10.8, 10.1, 9.0, 8.7, 7.9, 6.8, 5.8, 4.3, 3.4, 3.1, 2.8, 1.8, 21.9, 18.2, 17.9, 15.0, 13.8, 13.4, 12.4, 11.8, 9.2, 8.4, 7.1, 6.3, 5.9, 5.6, 5.3, 4.4, 4.2, 4.2, 4.1, 4.0, 3.8, 3.3, 47.2, 7.7, 3.5, 12.6, 5.5, 10.8, 33.2, 3.9, 5.6, 8.9, 21.9, 15.7, 12.7, 10.8],
    '승률(%)': [53.2, 53.8, 52.3, 45.2, 49.5, 48.1, 49.2, 52.0, 46.4, 40.9, 50.7, 46.3, 51.2, 47.0, 46.9, 49.7, 48.5, 45.8, 51.5, 51.0, 50.8, 51.1, 47.4, 50.2, 49.8, 48.2, 49.9, 52.3, 51.7, 47.2, 50.0, 53.7, 53.8, 51.8, 49.6, 49.2, 49.6, 45.3, 46.5, 54.4, 51.9, 49.9, 47.1, 43.6, 47.9, 47.0, 52.7, 47.8, 52.2, 52.3]
}
df = pd.DataFrame(data)

df['초상화'] = df['영웅'].apply(lambda x: hero_images.get(x, f"https://placehold.co/150x150/2b2d37/f99e1a/png?text={x}"))
df = df[['초상화', '영웅', '포지션', '세부역할', '픽률(%)', '승률(%)']]
df.to_csv('owtics_s21_exact_data.csv', index=False)

st.markdown("### 👑 CURRENT 1 TIER HEROES")
c1, c2, c3 = st.columns(3)
tank_top = df[df['포지션']=='탱커'].sort_values('픽률(%)', ascending=False).iloc[0]
dmg_top = df[df['포지션']=='딜러'].sort_values('픽률(%)', ascending=False).iloc[0]
sup_top = df[df['포지션']=='힐러'].sort_values('픽률(%)', ascending=False).iloc[0]

with c1:
    st.markdown(f"""<div class="tier-card tank-card"><img src="{tank_top['초상화']}" width="100" style="border-radius:50%; border: 3px solid #4EA8DE;"><p class="tier-title">{tank_top['영웅']}</p><p class="tier-stat">픽률 {tank_top['픽률(%)']}% | 승률 {tank_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="tier-card dmg-card"><img src="{dmg_top['초상화']}" width="100" style="border-radius:50%; border: 3px solid #F4556C;"><p class="tier-title">{dmg_top['영웅']}</p><p class="tier-stat">픽률 {dmg_top['픽률(%)']}% | 승률 {dmg_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="tier-card sup-card"><img src="{sup_top['초상화']}" width="100" style="border-radius:50%; border: 3px solid #38E09E;"><p class="tier-title">{sup_top['영웅']}</p><p class="tier-stat">픽률 {sup_top['픽률(%)']}% | 승률 {sup_top['승률(%)']}%</p></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 📋 FULL HERO LEADERBOARD")
html_table = "<table class='dark-table'><tr><th>FACE</th><th>영웅</th><th>포지션</th><th>세부역할</th><th>픽률(%)</th><th>승률(%)</th></tr>"
for index, row in df.iterrows():
    html_table += f"<tr><td><img src='{row['초상화']}' class='hero-img'></td><td>{row['영웅']}</td><td>{row['포지션']}</td><td>{row['세부역할']}</td><td>{row['픽률(%)']:.1f}</td><td>{row['승률(%)']:.1f}</td></tr>"
html_table += "</table>"
st.markdown(html_table, unsafe_allow_html=True)
