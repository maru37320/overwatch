import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SUPPORT HEROES", page_icon="💉", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Teko:wght@600&display=swap');
    h1, h2, h3 { font-family: 'Teko', sans-serif !important; font-style: italic; color: #38E09E !important; }
</style>
""", unsafe_allow_html=True)

st.title("💉 SUPPORT HERO ANALYSIS")

df = pd.read_csv('ow_data.csv')
sup_df = df[df['포지션'] == '힐러']

col1, col2 = st.columns(2)

with col1:
    st.subheader("PICK RATE RANKING")
    fig_pick = px.bar(
        sup_df.sort_values('픽률(%)', ascending=False),
        x='영웅', y='픽률(%)', text_auto='.1f',
        color_discrete_sequence=["#38E09E"]
    )
    fig_pick.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig_pick, use_container_width=True)

with col2:
    st.subheader("PICK RATE VS WIN RATE")
    fig_scatter = px.scatter(
        sup_df, x='픽률(%)', y='승률(%)', size='픽률(%)', hover_name='영웅',
        color_discrete_sequence=["#38E09E"]
    )
    fig_scatter.add_hline(y=50, line_dash="dash", line_color="#FF8C00", annotation_text="WIN RATE 50%")
    fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig_scatter, use_container_width=True)
