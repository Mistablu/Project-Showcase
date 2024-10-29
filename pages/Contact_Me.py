import streamlit as st

style_heading = "text-align: center"
st.markdown(f"<h1 style='{style_heading}'>Contact Me</h1>", 
            unsafe_allow_html=True)

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submit = st.form_submit_button()
    #if submit:
        