# import libraries
import streamlit as st
from functions import page_configs

# Page configurations
page_configs()
# st.set_page_config(layout='wide')

# Title
st.title('Welcome to Menuphi')

st.divider()

# Introduction
st.markdown(
    """
    Our aim at **Menuphi** is to reduce costs and increase profits
    by employing strategic menu engineering and data-driven insights,
    revolutionizing your restaurant's success by relieving you of the burden
    of menu analysis. Sit back, relax, and witness your profits soar!
    """
)

# 3-Step process
st.markdown(
    """
    ### To get started, follow this 3-step process:\n
    1. Download the menu data template.
    2. Fill it out with your menu item data.
    3. Upload the file and let **Menuphi** do the rest!
    """
)
