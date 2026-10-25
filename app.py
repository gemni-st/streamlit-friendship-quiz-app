import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Data App for Best Friend Quiz Results",
    page_icon=":bar_chart:",
    layout="wide",
)

with open("article.html", encoding="utf-8") as f:
    article_html = f.read()

components.html(article_html, height=2400, scrolling=True)
