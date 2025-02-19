import streamlit as st

def show_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Settings"])
    return page
