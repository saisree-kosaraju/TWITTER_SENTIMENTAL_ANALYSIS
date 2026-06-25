import streamlit as st
import plotly.graph_objects as go

from models.sentiment import get_sentiment, explain_sentiment
from components.charts import SENTIMENT_COLORS, PLOT_LAYOUT


def show_analyze():
    st.markdown('<div class="page-tag">Single Tweet Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Analyze a Tweet</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Paste any tweet and get instant sentiment analysis.</div>',
        unsafe_allow_html=True
    )

    tweet_input = st.text_area(
        "Tweet",
        placeholder="Example: I am very happy with this product!",
        height=150
    )

    if st.button("Analyze Sentiment"):
        if not tweet_input.strip():
            st.warning("Please enter a tweet first.")
            return

        sentiment, polarity, scores = get_sentiment(tweet_input)

        badge_class = {
            "Positive": "badge-positive",
            "Negative": "badge-negative",
            "Neutral": "badge-neutral"
        }[sentiment]

        emoji = {
            "Positive": "😊",
            "Negative": "😟",
            "Neutral": "😐"
        }[sentiment]

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(
            f'<span class="badge {badge_class}">{emoji} {sentiment}</span>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
### Polarity Score: `{polarity}`

**Positive Score:** `{scores["pos"]}`  
**Negative Score:** `{scores["neg"]}`  
**Neutral Score:** `{scores["neu"]}`
""")

        st.markdown(explain_sentiment(tweet_input))
        st.markdown('</div>', unsafe_allow_html=True)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=polarity,
            gauge={
                "axis": {"range": [-1, 1]},
                "bar": {"color": SENTIMENT_COLORS[sentiment]},
                "steps": [
                    {"range": [-1, -0.05], "color": "#f5d6d3"},
                    {"range": [-0.05, 0.05], "color": "#f3e8c8"},
                    {"range": [0.05, 1], "color": "#d9ead3"}
                ]
            }
        ))

        fig.update_layout(**PLOT_LAYOUT, height=300)
        st.plotly_chart(fig, use_container_width=True)