import streamlit as st

st.text_input("Your name", key = "name")
st.write("Welcome to you,", st.session_state.name)
