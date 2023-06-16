# import libraries
import streamlit as st
from functions import page_configs

# Page configurations
page_configs()
# st.set_page_config(layout='wide')

# Title
st.title('Welcome to Menuphi!')

st.divider()

# Introduction
st.markdown(
    """
    **Menuphi** was built with one goal in mind:
    lowering your costs and maximizing profits
    through strategic menu engineering and data-driven insights.
    """
)

st.markdown(
    """
    Let **Menuphi** revolutionize your restaurant's success,
    taking the burden of menu analysis off your hands.
    """
    )

st.markdown(
    """
    Sit back, relax, and watch your profits soar!
    """
)

# 3-Step process
st.markdown(
    """
    ### To get started, follow our easy 3-step process:\n
    1. Download the menu data template.
    2. Fill it out with your menu item data.
    3. Upload the file and let **Menuphi** do the rest!
    """
)
