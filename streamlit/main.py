import streamlit as st
import importlib

st.set_page_config(page_title="FinSight AI", layout="wide")

st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["AI Chatbot", "Financial Advisor", "PDF Analyzer"])

page_modules = {
    "AI Chatbot": "chatbot_app",
    "Financial Advisor": "financial_advisor",
    "PDF Analyzer": "pdf_analyser"
}

module = importlib.import_module(page_modules[page])
module.main()
