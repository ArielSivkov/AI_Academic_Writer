import streamlit as st
from components.sidebar import show_sidebar
from dashboard import show_dashboard
from components.settings import show_settings
import requests

st.title("AI Academic Writer")
st.write("Welcome to the AI Academic Writer. This tool helps you generate structured academic papers, ensures correct citations, fixes writing errors, and provides real-time feedback.")

page = show_sidebar()

if page == "Home":
    st.write("This is the home page.")
    st.header("Generate Academic Paper")
    with st.form(key='generate_paper_form'):
        topic = st.text_input("Enter the topic of the paper")
        submit_button = st.form_submit_button(label='Generate Paper')
        
        if submit_button:
            response = requests.get(f"http://localhost:8000/generate-paper?topic={topic}")
            if response.status_code == 200:
                st.write("Generated Paper:")
                st.write(response.json().get("paper"))
            else:
                st.write("Error generating paper.")
    
    st.header("Check Citations")
    with st.form(key='check_citations_form'):
        paper = st.text_area("Enter the paper to check citations")
        submit_button = st.form_submit_button(label='Check Citations')
        
        if submit_button:
            response = requests.get(f"http://localhost:8000/check-citations?paper={paper}")
            if response.status_code == 200:
                st.write("Citations Valid:")
                st.write(response.json().get("citations_valid"))
            else:
                st.write("Error checking citations.")
    
    st.header("Check Plagiarism")
    with st.form(key='check_plagiarism_form'):
        paper = st.text_area("Enter the paper to check for plagiarism")
        submit_button = st.form_submit_button(label='Check Plagiarism')
        
        if submit_button:
            response = requests.get(f"http://localhost:8000/check-plagiarism?paper={paper}")
            if response.status_code == 200:
                st.write("Plagiarism Detected:")
                st.write(response.json().get("plagiarism_detected"))
            else:
                st.write("Error checking plagiarism.")
    
    st.header("Analyze Feedback")
    with st.form(key='analyze_feedback_form'):
        paper = st.text_area("Enter the paper to analyze feedback")
        submit_button = st.form_submit_button(label='Analyze Feedback')
        
        if submit_button:
            response = requests.get(f"http://localhost:8000/analyze-feedback?paper={paper}")
            if response.status_code == 200:
                st.write("Feedback:")
                st.write(response.json().get("feedback"))
            else:
                st.write("Error analyzing feedback.")
elif page == "Dashboard":
    show_dashboard()
elif page == "Settings":
    show_settings()
