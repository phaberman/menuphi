# import libraries
import streamlit as st
from functions import page_configs

# Page configurations
page_configs()

# Customer quotes on the side bar
st.sidebar.markdown(
    """
    ## Customer Reviews
    *Menuphi's quick analysis has been a game-changer for us!* - Tom, CEO of The Burger Barn
    \n
    *Thanks to Menuphi, we now have a data-driven menu strategy that's driving customer satisfaction.* - Alex, General Manager of The Olive Tree
    \n
    *Menuphi simplified our menu analysis and saved us valuable time and resources.* - Lisa, Restaurant Owner of The Spice House
    """
    )

# Title
st.title('Menuphi')
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
