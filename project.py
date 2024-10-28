import streamlit as st
#python -m streamlit run project.py
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(r"images\1.png")

with col2:
    st.title("My Projects")
    content = "ALLOT"
    st.info(content)