
import streamlit as st

st.set_page_config(page_title="My Python Website")

st.title("Welcome to My Website")

st.write("My Python website is successfully online!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter your name.")
