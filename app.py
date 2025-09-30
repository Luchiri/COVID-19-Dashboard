import streamlit as st
from pathlib import Path
from data_loader import load_data
import pandas as pd
import datetime
import plotly.express as px

# --- Page config ---
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# --- Logo ---
st.title("COVID-19 Dashboard 🌍")
logo_path = Path("assets/logo.png")
if logo_path.exists():
    st.image(str(logo_path), width=120)

# --- Load data ---
df = load_data()

if df.empty:
    st.warning("No data available.")
else:
    st.success(f"Loaded {len(df):,} rows ✅")

    # --- Sidebar filters ---
    st.sidebar.header("Filters")
    countries = df["location"].unique()
    selected_country = st.sidebar.selectbox("Select Country", sorted(countries))

    # Convert pandas Timestamps to Python datetime for the slider
    min_date = df["date"].min().to_pydatetime()
    max_date = df["date"].max().to_pydatetime()

    selected_date = st.sidebar.slider(
        "Select Date Range",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date)
    )

    # Filter dataframe based on country and date
    mask = (
        (df["location"] == selected_country) &
        (df["date"] >= pd.Timestamp(selected_date[0])) &
        (df["date"] <= pd.Timestamp(selected_date[1]))
    )
    filtered_df = df[mask]

    # --- Display country flag ---
    iso3_code = df[df["location"] == selected_country]["iso_code"].iloc[0]
    flag_path = Path(f"assets/flags/{iso3_code}.png")
    if flag_path.exists():
        st.image(str(flag_path), width=60)

    # --- Summary metrics ---
    st.markdown(f"## COVID-19 Summary for {selected_country}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cases", int(filtered_df["total_cases"].max() or 0))
    col2.metric("New Cases", int(filtered_df["new_cases"].sum() or 0))
    col3.metric("Total Deaths", int(filtered_df["total_deaths"].max() or 0))
    col4.metric("New Deaths", int(filtered_df["new_deaths"].sum() or 0))

    # --- Data preview ---
    st.markdown("### Data Table")
    st.dataframe(filtered_df)

# --- Line chart for Total Cases ---
st.markdown(f"### Total Cases Over Time for {selected_country}")
fig_total = px.line(
    filtered_df,
    x="date",
    y="total_cases",
    title=f"Total COVID-19 Cases in {selected_country}",
    labels={"date": "Date", "total_cases": "Total Cases"},
)
st.plotly_chart(fig_total, use_container_width=True)

# --- Line chart for New Cases ---
st.markdown(f"### New Cases Over Time for {selected_country}")
fig_new = px.line(
    filtered_df,
    x="date",
    y="new_cases",
    title=f"New COVID-19 Cases in {selected_country}",
    labels={"date": "Date", "new_cases": "New Cases"},
)
st.plotly_chart(fig_new, use_container_width=True)

# --- Bar chart for New Deaths ---
st.markdown(f"### New Deaths Over Time for {selected_country}")
fig_deaths = px.bar(
    filtered_df,
    x="date",
    y="new_deaths",
    title=f"New COVID-19 Deaths in {selected_country}",
    labels={"date": "Date", "new_deaths": "New Deaths"},
)
st.plotly_chart(fig_deaths, use_container_width=True)
