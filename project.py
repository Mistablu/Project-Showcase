import streamlit as st
import pandas
#python -m streamlit run project.py
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(r"images\1.png")

with col2:
    st.title("My Projects")
    content = "ALLOT"
    st.info(content)
st.write("Below you can find some of the apps i have built, please feel free to contact me")

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])