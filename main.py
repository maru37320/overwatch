import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정 (다크 테마에 어울리게 설정)
st.set_page_config(page_title="OVERWATCH META DASHBOARD", page_icon="오버워치", layout="wide")

# 2. 오버워치 스타일 커스텀 CSS 주입
st.markdown("""
<style>
    /* 오버워치 특유의 이탤릭 굵은 폰트 느낌과 오렌지색 포인트 */
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@600&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Malgun Gothic', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Teko', sans-serif !important;
        font-style: italic;
        color: #FF8C00 !important; /* 오버워치 오렌지 */
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stProgress > div > div > div > div {
        background-color: #FF8C00;
    }
</style>
""", unsafe_allow_html=True)

st.title("OVERWATCH 2 META DASHBOARD")
st.markdown("### CURRENT SEASON HERO STATISTICS")
st.markdown("도미나, 제트팩 캣, 안란, 우양, 엠레 등 모든 영웅들의 최신 픽률과 승률을 분석합니다.")

st.divider()

# 3. 영웅 로스터 대폭 추가 (엠레 포함)
data = {
    '영웅': [
        # 탱커 (13)
        '도미나', '라인하르트', '디바', '윈스턴', '오리사', '자리야', '시그마', '라마트라', '마우가', '둠피스트', '레킹볼', '로드호그', '정커퀸',
        # 딜러 (21)
        '안란', '엠레', '겐지', '트레이서', '캐서디', '솔저: 76', '위도우메이커', '애쉬', '소전', '에코', '파라', '리퍼', '메이', '솜브라', '한조', '벤처', '바스티온', '정크랫', '시메트라', '토르비욘', '일리아리',
        # 힐러 (11)
        '제트팩 캣', '우양', '아나', '키리코', '메르시', '루시우', '모이라', '바티스트', '브리기테', '라이프위버', '젠야타'
    ],
    '포지션': [
        '탱커']*13 + ['딜러']*21 + ['힐러']*11,
    '픽률(%)': [
        11.2, 8.0, 7.2, 5.5, 4.0, 4.5, 6.1, 5.8, 4.2, 5.0, 3.1, 4.8, 4.0,
        10.5, 9.8, 7.5, 6.4, 5.9, 4.8, 4.2, 5.1, 4.5, 3.8, 3.5, 4.0, 3.2, 4.1, 3.9, 3.5, 2.5, 3.0, 2.1, 2.8, 3.3,
        13.1, 9.5, 12.5, 9.8, 8.2, 5.1, 6.0, 5.5, 4.0, 3.5, 4.8
    ],
    '승률(%)': [
        51.2, 53.1, 51.5, 48.2, 50.0, 52.0, 51.8, 49.5, 48.0, 49.2, 50.1, 49.8, 51.0,
        52.1, 51.8, 48.8, 52.3, 49.0, 50.5, 47.5, 51.0, 50.2, 49.8, 52.5, 48.5, 51.2, 49.0, 48.5, 50.0, 47.0, 49.5, 53.0, 51.1, 49.2,
        50.8, 51.5, 49.5, 51.2, 50.1, 51.0, 49.9, 50.5, 52.1, 48.5, 51.5
    ]
}
df = pd.DataFrame(data)

# CSV 파일로 저장해두기 (다른 페이지에서 불러오기 위함)
df.to_csv('ow_data.csv', index=False)

st.subheader("OVERALL HERO USAGE (TREEMAP)")
role_colors = {'힐러': '#38E09E', '딜러': '#F4556C', '탱커': '#4EA8DE'}

# 다크 테마에 맞는 그래프 디자인 적용
fig_tree = px.treemap(
    df, path=['포지션', '영웅'], values='픽률(%)', color='포지션',
    color_discrete_map=role_colors
)
fig_tree.update_layout(
    margin=dict(t=20, l=10, r=10, b=10),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)
st.plotly_chart(fig_tree, use_container_width=True)
