import streamlit as st

def kpi_cards(total, positive, negative, neutral):
    pct_pos = f"{positive / total * 100:.1f}%" if total else "0%"
    pct_neg = f"{negative / total * 100:.1f}%" if total else "0%"
    pct_neu = f"{neutral / total * 100:.1f}%" if total else "0%"

    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-value">{total}</div>
            <div class="kpi-label">Total Tweets</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">{positive}</div>
            <div class="kpi-label">Positive · {pct_pos}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">{negative}</div>
            <div class="kpi-label">Negative · {pct_neg}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">{neutral}</div>
            <div class="kpi-label">Neutral · {pct_neu}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)