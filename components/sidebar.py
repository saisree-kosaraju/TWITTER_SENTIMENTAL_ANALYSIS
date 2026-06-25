import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="logo-box">
            <div class="logo-title">📊 SentimentIQ</div>
            <div class="logo-subtitle">Twitter Sentiment Analysis Platform</div>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio(
            "Navigation",
            ["Dashboard", "Analyze Tweet", "AI Chatbot"]
        )

        st.markdown('<div class="section-title">Data Source</div>', unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Upload tweets.csv",
            type=["csv"]
        )

        st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)

        st.write(
            "This project uses VADER NLP, trained ML model support, "
            "and Gemini chatbot with offline fallback."
        )

    return page, uploaded_file