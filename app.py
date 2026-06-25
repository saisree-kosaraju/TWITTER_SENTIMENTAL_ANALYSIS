import streamlit as st
import pandas as pd

from components.sidebar import show_sidebar
from views.Dashboard import show_dashboard
from views.Analyze import show_analyze
from views.Chatbot import show_chatbot


st.set_page_config(
    page_title="SentimentIQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

page, uploaded_file = show_sidebar()

if uploaded_file:
    df = pd.read_csv(uploaded_file, header=None)

    if df.shape[1] >= 4:
        df = df.iloc[:, [1, 2, 3]]
        df.columns = ["entity", "label", "tweet"]
    else:
        st.error("Uploaded CSV format is not supported.")
        st.stop()
else:
    df = pd.read_csv("data/tweets.csv")

if "tweet" not in df.columns:
    st.error("CSV file must contain tweet text.")
    st.stop()

df = df.dropna(subset=["tweet"])

if page == "Dashboard":
    show_dashboard(df)
elif page == "Analyze Tweet":
    show_analyze()
elif page == "AI Chatbot":
    show_chatbot()