# dashboard/app.py

import streamlit as st
import pandas as pd
import requests
import os

# Page config
st.set_page_config(page_title="Skippio Heatmap", layout="wide")
st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

# Logo + Title
col1, col2 = st.columns([6, 1])
with col2:
   logo_path = os.path.join(os.path.dirname(__file__), "skippio_logo.png")
   st.image(logo_path, width=120)
with col1:
    st.markdown("<h1 style='margin-bottom:0;color:#3DC7A4;'>Skippio Venue Heatmap</h1>", unsafe_allow_html=True)
    st.caption("Live order activity, performance, and venue analytics")

API_URL = "http://127.0.0.1:8000/orders"  # update for deployment

def load_data():
    try:
        res = requests.get(API_URL)
        return pd.DataFrame(res.json()) if res.status_code == 200 else pd.DataFrame()
    except:
        return pd.DataFrame()

data = load_data()

st.markdown("""
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}
</style>
""", unsafe_allow_html=True)


if not data.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔥 Orders by Section")
        section_counts = data['section'].value_counts().reset_index()
        section_counts.columns = ['Section', 'Orders']
        st.bar_chart(section_counts.set_index('Section'))

    with col2:
        st.subheader("🍔 Popular Items")
        item_counts = data['item'].value_counts().reset_index()
        item_counts.columns = ['Item', 'Count']
        st.bar_chart(item_counts.set_index('Item'))

    st.subheader("⏱️ Vendor Wait Time")
    vendor_stats = data.groupby('vendor')['wait_time'].mean().round(2).reset_index()
    vendor_stats.columns = ['Vendor', 'Avg Wait Time (min)']
    st.dataframe(vendor_stats, use_container_width=True)

    with st.expander("📋 View Raw Data"):
        st.dataframe(data)
else:
    st.warning("No order data available yet.")