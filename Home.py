# import libraries
import streamlit as st
from functions import page_configs

# Page configurations
page_configs()
# st.set_page_config(layout='wide')

# Title
st.markdown('# Menuphi')
st.markdown('###### *Menu Analysis Made Easy*')


st.divider()

# Introduction
st.markdown(
    """
    ### What is **Menuphi?**\n
    **Menuphi** helps restuarants reduce costs and increase profits
    by employing strategic menu engineering and data-driven insights,
    revolutionizing your restaurant's success by relieving you of the burden
    of menu analysis.
    """
)

# 3-Step process
st.markdown(
    """
    ### Getting started is as easy as 1, 2, 3...\n
    1. Download the menu data template.
    2. Fill it out with your menu item data.
    3. Upload the file and let **Menuphi** do the rest!
    """
)
