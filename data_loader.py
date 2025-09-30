import pandas as pd
import streamlit as st
from pathlib import Path

DATA_FILE = Path("owid-covid-data.csv")

@st.cache_data
def load_data():
    """Load COVID-19 data from local CSV file."""
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE, parse_dates=["date"])
        return df
    else:
        st.error("Local CSV file not found. Please add owid-covid-data.csv to the project folder.")
        return pd.DataFrame()
