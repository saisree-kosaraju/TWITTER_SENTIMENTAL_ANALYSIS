import plotly.express as px

SENTIMENT_COLORS = {
    "Positive": "#2e7d32",
    "Negative": "#b3261e",
    "Neutral": "#8b6f00"
}

PLOT_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#4a3527",
    margin=dict(t=35, b=25, l=25, r=25)
)

def pie_chart(sentiment_count):
    fig = px.pie(
        sentiment_count,
        names="Sentiment",
        values="Count",
        hole=0.58,
        color="Sentiment",
        color_discrete_map=SENTIMENT_COLORS
    )
    fig.update_layout(**PLOT_LAYOUT)
    return fig

def bar_chart(sentiment_count):
    fig = px.bar(
        sentiment_count,
        x="Sentiment",
        y="Count",
        text="Count",
        color="Sentiment",
        color_discrete_map=SENTIMENT_COLORS
    )
    fig.update_layout(**PLOT_LAYOUT, showlegend=False)
    return fig

def polarity_histogram(df):
    fig = px.histogram(
        df,
        x="Polarity",
        nbins=25,
        color_discrete_sequence=["#8b6f47"]
    )
    fig.add_vline(x=0, line_dash="dash", line_color="#5d4037")
    fig.update_layout(**PLOT_LAYOUT, height=280)
    return fig