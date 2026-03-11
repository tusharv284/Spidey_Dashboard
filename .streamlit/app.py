import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="🕷️ Spider‑Verse Dashboard",
    page_icon="🕸️",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
spidey_css = """
<style>
/* Global background (fallback if no image) */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #2B3784 0%, #030104 55%, #000000 100%);
}

/* Optional: dim top menu/footer */
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(3,1,4,0.3);
}

/* Main cards */
.spidey-card {
    border-radius: 16px;
    padding: 18px 20px;
    background: rgba(3,1,4,0.85);
    border: 1px solid #DF1F2D;
    box-shadow: 0 0 20px rgba(223,31,45,0.5), 0 0 40px rgba(43,55,132,0.6) inset;
    position: relative;
    overflow: hidden;
}

/* Web overlay lines in cards */
.spidey-card::before,
.spidey-card::after {
    content: "";
    position: absolute;
    width: 200%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #DF1F2D, #447BBE, transparent);
    opacity: 0.25;
}

.spidey-card::before {
    top: 15%;
    left: -50%;
    transform: rotate(12deg);
}

.spidey-card::after {
    bottom: 10%;
    left: -40%;
    transform: rotate(-18deg);
}

/* Headline */
.spidey-title {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    background: linear-gradient(120deg, #DF1F2D, #447BBE, #FFD700);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 12px rgba(223,31,45,0.7);
}

/* Subtitle */
.spidey-subtitle {
    font-size: 14px;
    letter-spacing: 1px;
    color: #E2E2E2;
}

/* Metric label and value */
.spidey-metric-label {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #abadbf;
}

.spidey-metric-value {
    font-size: 26px;
    font-weight: 700;
    background: linear-gradient(90deg, #FFD700, #FFFFFF);
    -webkit-background-clip: text;
    color: transparent;
}

/* "Spider Sense" chip */
.spider-sense-chip {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid #FF4081;
    color: #FF4081;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Tabs */
button[kind="secondary"] {
    border-radius: 999px !important;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #030104 0%, #0E1117 60%, #030104 100%);
    border-right: 1px solid rgba(223,31,45,0.6);
}
</style>
"""
st.markdown(spidey_css, unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🕸️ Spider‑Filters")
    st.caption("Tune your view of the **Spider‑Verse**.")
    view = st.selectbox(
        "Choose universe",
        ["Earth‑616", "Earth‑1610 (Miles)", "Spider‑Gwen", "Spider‑Noir", "Across the Spider‑Verse"]
    )
    intensity = st.slider("Spider‑Sense intensity", 0, 100, 60)
    show_alt = st.checkbox("Show alternate timelines", True)
    st.markdown("---")
    st.write("Data date:", datetime.today().strftime("%d %b %Y"))
    st.markdown("Made with ❤️ in the **Spider‑Verse**")

# ---------- MOCK DATA ----------
np.random.seed(42)
days = pd.date_range(end=datetime.today(), periods=30)
traffic = np.random.randint(80, 250, size=30)
threats = np.random.randint(0, 40, size=30)
saves = np.random.randint(5, 60, size=30)

df = pd.DataFrame({
    "Date": days,
    "City Web Traffic": traffic,
    "Threat Level": threats,
    "Citizens Saved": saves
})

df["Universe"] = np.random.choice(
    ["Earth‑616", "Earth‑1610 (Miles)", "Spider‑Gwen", "Spider‑Noir"],
    size=len(df)
)

if view != "Across the Spider‑Verse":
    df_filtered = df[df["Universe"] == view]
else:
    df_filtered = df.copy()

# ---------- HEADER ----------
st.markdown(
    """
    <div class="spidey-card">
        <div class="spidey-title">Spider‑Verse Intelligence Hub</div>
        <div class="spidey-subtitle">
            Live analytics from New York's rooftops — tracking threat levels, web‑swing traffic, and hero saves across the multiverse.
        </div>
        <div style="margin-top:10px;">
            <span class="spider-sense-chip">Spider‑Sense: online</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("")

# ---------- TOP METRICS ----------
col1, col2, col3, col4 = st.columns(4)

total_traffic = int(df_filtered["City Web Traffic"].sum())
avg_threat = float(df_filtered["Threat Level"].mean())
total_saves = int(df_filtered["Citizens Saved"].sum())
max_threat_day = df_filtered.loc[df_filtered["Threat Level"].idxmax(), "Date"].strftime("%d %b")

with col1:
    st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
    st.markdown('<div class="spidey-metric-label">WEB TRAFFIC (LAST 30D)</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="spidey-metric-value">{total_traffic:,}</div>', unsafe_allow_html=True)
    st.caption("How many swings across the skyline.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
    st.markdown('<div class="spidey-metric-label">AVG THREAT LEVEL</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="spidey-metric-value">{avg_threat:.1f} / 40</div>', unsafe_allow_html=True)
    st.caption("Higher means more villains to web up.")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
    st.markdown('<div class="spidey-metric-label">CITIZENS SAVED</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="spidey-metric-value">{total_saves:,}</div>', unsafe_allow_html=True)
    st.caption("Because with great power comes great responsibility.")
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
    st.markdown('<div class="spidey-metric-label">PEAK THREAT DAY</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="spidey-metric-value">{max_threat_day}</div>', unsafe_allow_html=True)
    st.caption("When everything went sideways in the city.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("")

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(["📈 Web‑Swing Trends", "🧬 Threat Heatmap", "🕷️ Multiverse Table"])

# Tab 1: Line charts
with tab1:
    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
        fig1 = px.line(
            df_filtered,
            x="Date",
            y="City Web Traffic",
            title="Daily Web‑Swing Traffic",
            color_discrete_sequence=["#447BBE"]
        )
        fig1.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
        fig2 = px.line(
            df_filtered,
            x="Date",
            y="Threat Level",
            title="Threat Level Over Time",
            color_discrete_sequence=["#DF1F2D"]
        )
        fig2.update_traces(fill="tozeroy", fillcolor="rgba(223,31,45,0.3)")
        fig2.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Tab 2: Heatmap / bar
with tab2:
    st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
    df_hm = df_filtered.copy()
    df_hm["Day"] = df_hm["Date"].dt.day
    df_hm["Weekday"] = df_hm["Date"].dt.day_name()

    pivot = df_hm.pivot_table(
        index="Weekday",
        columns="Day",
        values="Threat Level",
        aggfunc="mean"
    )

    fig_hm = go.Figure(
        data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns,
            y=pivot.index,
            colorscale=[
                [0, "#030104"],
                [0.4, "#2B3784"],
                [0.7, "#DF1F2D"],
                [1, "#FFD700"]
            ],
            colorbar=dict(title="Threat")
        )
    )
    fig_hm.update_layout(
        title="Spider‑Sense Threat Map",
        xaxis_title="Day of Month",
        yaxis_title="Weekday",
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_hm, use_container_width=True)
    st.caption("Bright red/gold squares are when the city really needed Spider‑Man.")
    st.markdown("</div>", unsafe_allow_html=True)

# Tab 3: Data table
with tab3:
    st.markdown('<div class="spidey-card">', unsafe_allow_html=True)
    st.write("Raw Spider‑Verse event log")
    st.dataframe(
        df_filtered.sort_values("Date", ascending=False).reset_index(drop=True),
        use_container_width=True,
        height=420
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <p style="text-align:center; margin-top:20px; font-size:12px; color:#abadbf;">
    🕸️ Friendly Neighborhood Dashboard • Inspired by Spider‑Man comics & films
    </p>
    """,
    unsafe_allow_html=True
)
