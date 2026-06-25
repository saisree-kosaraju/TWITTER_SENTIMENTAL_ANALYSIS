import streamlit as st
from models.gemini import gemini_reply


def show_chatbot():
    st.markdown('<div class="page-tag">Conversational Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">AI Sentiment Chatbot</div>', unsafe_allow_html=True)
    st.markdown(
    '<div class="page-subtitle">Offline AI-style chatbot powered by ML and VADER sentiment analysis.</div>',
    unsafe_allow_html=True
)

    st.markdown("""
    <div class="info-card">
    <b>How to use:</b> Type any tweet below and press Enter.
    The chatbot will explain sentiment, emotion, reason, polarity score, and suggestion.
    </div>
    """, unsafe_allow_html=True)

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    if not st.session_state.chat_messages:
        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": "Hi! 👋 I am SentimentIQ. Type a tweet and I will analyze its sentiment."
        })

    for message in st.session_state.chat_messages:
        with st.chat_message(
            message["role"],
            avatar="📊" if message["role"] == "assistant" else "👤"
        ):
            st.markdown(message["content"])

    user_input = st.chat_input("Type your tweet here and press Enter")

    if user_input:
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

        reply = gemini_reply(user_input)

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": reply
        })

        with st.chat_message("assistant", avatar="📊"):
            st.markdown(reply)

    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        if st.button("Clear Chat"):
            st.session_state.chat_messages = []
            st.rerun()

    with col2:
        chat_text = "\n\n".join(
            f"{msg['role'].upper()}:\n{msg['content']}"
            for msg in st.session_state.chat_messages
        )

        st.download_button(
            "Export Chat",
            chat_text,
            "chat_history.txt",
            "text/plain"
        )