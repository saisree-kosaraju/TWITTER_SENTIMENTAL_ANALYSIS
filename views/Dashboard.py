import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from models.sentiment import get_sentiment


COLORS = {
    "Positive": "#7ed957",
    "Negative": "#ff5c5c",
    "Neutral": "#ff9f1c"
}


def donut_chart(labels, values, title_text):
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.62,
                marker=dict(colors=[COLORS["Positive"], COLORS["Negative"], COLORS["Neutral"]]),
                textinfo="percent",
                textfont=dict(color="white", size=14)
            )
        ]
    )

    fig.update_layout(
        height=280,
        paper_bgcolor="#0d213a",
        plot_bgcolor="#0d213a",
        font_color="white",
        margin=dict(t=20, b=20, l=20, r=20),
        showlegend=False,
        annotations=[
            dict(
                text=title_text,
                x=0.5,
                y=0.5,
                font=dict(size=26, color="white"),
                showarrow=False
            )
        ]
    )

    return fig


def gauge_chart(value):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            number={"font": {"size": 38, "color": "white"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "white"},
                "bar": {"color": "#ffc857"},
                "bgcolor": "#0d213a",
                "steps": [
                    {"range": [0, 40], "color": "#ff5c5c"},
                    {"range": [40, 70], "color": "#ff9f1c"},
                    {"range": [70, 100], "color": "#7ed957"},
                ],
            },
        )
    )

    fig.update_layout(
        height=280,
        paper_bgcolor="#0d213a",
        font_color="white",
        margin=dict(t=20, b=20, l=20, r=20)
    )

    return fig


def show_dashboard(df):
    st.markdown('<div class="page-tag">TWITTER SENTIMENT INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Tweet Sentiment Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Professional dashboard for analyzing tweet sentiment, public opinion, and engagement insights.</div>',
        unsafe_allow_html=True
    )

    df[["Sentiment", "Polarity", "_scores"]] = df["tweet"].apply(
        lambda text: pd.Series(get_sentiment(text))
    )

    total = len(df)
    positive = int((df["Sentiment"] == "Positive").sum())
    negative = int((df["Sentiment"] == "Negative").sum())
    neutral = int((df["Sentiment"] == "Neutral").sum())

    positive_pct = round((positive / total) * 100, 1) if total else 0
    negative_pct = round((negative / total) * 100, 1) if total else 0
    neutral_pct = round((neutral / total) * 100, 1) if total else 0

    sentiment_score = round(positive_pct - negative_pct + 50, 1)
    sentiment_score = max(0, min(100, sentiment_score))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Tweet Sentiment Score</div>
                <div class="kpi-sub">Live Sentiment Index</div>
                <div class="kpi-value">{sentiment_score}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Tweets Analyzed</div>
                <div class="kpi-sub">Total Dataset Size</div>
                <div class="kpi-value">{total}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">Public Opinion</div>
                <div class="kpi-sub">Positive Share</div>
                <div class="kpi-value">{positive_pct}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">SENTIMENT VISUALIZATION</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="chart-title">Tweet Sentiment Mix</div>', unsafe_allow_html=True)
        st.plotly_chart(
            donut_chart(
                ["Positive", "Negative", "Neutral"],
                [positive, negative, neutral],
                f"{total}"
            ),
            use_container_width=True
        )

    with c2:
        st.markdown('<div class="chart-title">Overall Sentiment</div>', unsafe_allow_html=True)
        st.plotly_chart(
            donut_chart(
                ["Positive", "Negative", "Neutral"],
                [positive_pct, negative_pct, neutral_pct],
                f"{sentiment_score}%"
            ),
            use_container_width=True
        )

    with c3:
        st.markdown('<div class="chart-title">Public Opinion Score</div>', unsafe_allow_html=True)
        st.plotly_chart(
            gauge_chart(sentiment_score),
            use_container_width=True
        )

    st.markdown('<div class="section-title">SENTIMENT DISTRIBUTION</div>', unsafe_allow_html=True)

    sentiment_df = pd.DataFrame({
        "Sentiment": ["Positive", "Negative", "Neutral"],
        "Count": [positive, negative, neutral],
        "Percentage": [positive_pct, negative_pct, neutral_pct]
    })

    fig_bar = px.bar(
        sentiment_df,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        text="Count",
        color_discrete_map=COLORS
    )

    fig_bar.update_layout(
        height=320,
        paper_bgcolor="#0d213a",
        plot_bgcolor="#0d213a",
        font_color="white",
        margin=dict(t=30, b=30, l=30, r=30),
        showlegend=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="#24456d")
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown('<div class="section-title">TWEET-LEVEL SENTIMENT RESULTS</div>', unsafe_allow_html=True)

    display_df = df[["tweet", "Sentiment", "Polarity"]].copy()
    display_df.columns = ["Tweet", "Sentiment", "Polarity Score"]

    st.dataframe(display_df, use_container_width=True, height=350)

    csv = display_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Tweet Sentiment Report",
        csv,
        "tweet_sentiment_report.csv",
        "text/csv"
    )