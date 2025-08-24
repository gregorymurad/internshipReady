# app.py — Water Quality Dashboard (Streamlit)
# -------------------------------------------------------------
# Features
# - Upload CSV (or auto-generate a realistic demo dataset)
# - Smart column detection (time, lat, lon, station)
# - Sidebar filters: date range, station, parameter, rolling window, outlier removal
# - KPI summary cards
# - Interactive map (OpenStreetMap, no token needed)
# - Time series with optional rolling mean
# - Box/violin plots, scatter w/ trendline, correlation heatmap
# - Basic threshold alerts (DO, pH, turbidity, chlorophyll, temperature)
# - Anomaly flags (z-score based)
# - Download filtered data
# -------------------------------------------------------------


import io
import json
import math
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Water Quality Dashboard",
    page_icon="💧",
    layout="wide",
)

# --------------------------
# Utilities & Config
# --------------------------

NUMERIC_PARAM_CANDIDATES = [
    ("temperature", "°F"),
    ("salinity", "psu"),
    ("dissolved_oxygen", "mg/L"),
    ("do", "mg/L"),
    ("oxygen", "mg/L"),
    ("ph", "pH"),
    ("turbidity", "NTU"),
    ("chlorophyll", "µg/L"),
    ("chl", "µg/L"),
    ("conductivity", "µS/cm"),
]

DEFAULT_THRESHOLDS = {
    # Basic, non-regulatory heuristics for quick alerts
    "dissolved_oxygen": {"min": 5},          # mg/L
    "do": {"min": 5},                        # alias
    "ph": {"min": 6.5, "max": 8.5},
    "turbidity": {"max": 50},               # NTU
    "chlorophyll": {"max": 20},             # µg/L
    "temperature": {"max": 32},             # °C
}

@st.cache_data(show_spinner=False)
def generate_demo_data(n_days: int = 7, freq_min: int = 30, n_stations: int = 4) -> pd.DataFrame:
    """Create a synthetic but realistic dataset for quick demo/testing."""
    rng = pd.date_range(
        end=pd.Timestamp.utcnow().floor("min"),
        periods=(n_days * 24 * 60) // freq_min,
        freq=f"{freq_min}min",
        tz="UTC",
    )
    base_lat, base_lon = 25.7617, -80.1918  # Miami-ish
    stations = [f"STN-{i+1:02d}" for i in range(n_stations)]

    rows = []
    for stn in stations:
        lat_jitter = np.random.uniform(-0.15, 0.15)
        lon_jitter = np.random.uniform(-0.15, 0.15)
        lat = base_lat + lat_jitter
        lon = base_lon + lon_jitter

        # Seasonal-ish variation
        temp = 27 + 3 * np.sin(np.linspace(0, 6 * np.pi, len(rng))) + np.random.normal(0, 0.6, len(rng))
        sal = 35 + 1.0 * np.sin(np.linspace(0, 3 * np.pi, len(rng))) + np.random.normal(0, 0.3, len(rng))
        do = 6.5 + 0.8 * np.cos(np.linspace(0, 4 * np.pi, len(rng))) + np.random.normal(0, 0.25, len(rng))
        ph = 7.9 + 0.1 * np.sin(np.linspace(0, 2 * np.pi, len(rng))) + np.random.normal(0, 0.03, len(rng))
        chl = 10 + 4 * np.maximum(0, np.sin(np.linspace(0, 5 * np.pi, len(rng)))) + np.random.normal(0, 1.2, len(rng))
        turb = 8 + 6 * np.maximum(0, np.cos(np.linspace(0, 5 * np.pi, len(rng)))) + np.random.normal(0, 1.5, len(rng))

        df_stn = pd.DataFrame({
            "timestamp": rng,
            "station": stn,
            "latitude": lat,
            "longitude": lon,
            "temperature": temp,
            "salinity": sal,
            "dissolved_oxygen": do,
            "ph": ph,
            "chlorophyll": chl,
            "turbidity": turb,
        })
        rows.append(df_stn)

    df = pd.concat(rows, ignore_index=True)
    return df


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Lower-case + strip spaces/units from column names for easier matching."""
    mapping = {c: c.lower().strip().replace(" ", "_") for c in df.columns}
    df = df.rename(columns=mapping)
    return df


def detect_columns(df: pd.DataFrame):
    """Detect standard columns and candidate numeric parameters."""
    cols = {c: c.lower() for c in df.columns}

    # Time
    time_col = None
    for c in df.columns:
        if any(k in c.lower() for k in ["time", "date"]):
            time_col = c
            break
    if time_col is None and "timestamp" in cols.values():
        time_col = [k for k, v in cols.items() if v == "timestamp"][0]

    # Latitude/Longitude
    lat_col = None
    lon_col = None
    for c in df.columns:
        lc = c.lower()
        if "lat" in lc and lat_col is None:
            lat_col = c
        if ("lon" in lc or "lng" in lc or "long" in lc) and lon_col is None:
            lon_col = c

    # Station name/id
    station_col = None
