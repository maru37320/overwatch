import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="딜러 분석", page_icon="⚔️", layout="wide")

st.title("⚔️ 딜러 (Damage) 영웅 분석")
st.markdown("현재 시즌 **딜러** 영웅들의 사용률과 승률 데이터야.")

# 딜러 전용 데이터
data = {
    '영웅': ['겐지', '트레이서', '캐서디', '솔저: 76', '위도우메이커'],
    '픽률(%)': [7.5, 6.4, 5.9, 4.8, 4.2],
    '승률(%)': [48.8, 52.3, 49.0, 50.5, 47.5]
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 딜러 픽률 순위")
    fig_pick = px.bar(
        df.sort_values('픽률(%)', ascending=False),
        x='영웅', y='픽률(%)', text_auto='.1f',
        color_discrete_sequence=["#F4556C"] # 빨간색
    )
    fig_pick.update_layout(xaxis_title="", yaxis_title="픽률 (%)")
    st.plotly_chart(fig_pick, use_container_width=True)

with col2:
    st.subheader("🎯 픽률 vs 승률 상관관계")
    fig_scatter = px.scatter(
        df, x='픽률(%)', y='승률(%)', size='픽률(%)',
        hover_name='영웅', color_discrete_sequence=["#F4556C"]
    )
    fig_scatter.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="승률 50%")
    st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("📋 상세 데이터")
st.dataframe(df.sort_values('픽률(%)', ascending=False).reset_index(drop=True), use_container_width=True)
