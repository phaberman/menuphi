import streamlit as st
from functions import file_downloader
import pandas as pd

# Title
st.title('Download Our Template')

st.divider()

# Introduction
st.markdown(
    """
    To get started, download the **Menu Data Template**
    and fill it out with your menu item data.
    Each row represents one menu item, so if your menu contains 10 items,
    there should be 10 rows (excluding the column headers).\n
    Here is an example of what the first row should look like:
    """
)

### Dataframe for example ###

# Create data
data = {
    'Menu Category': ['Burgers'],
    'Item Name': ['Classic Burger'],
    'Menu Price': ['8.99'],
    'Cost': ['2.45'],
    'Number Sold': ['750']
}

# Create dataframe
df = pd.DataFrame(data)

# Display dataframe on page
st.dataframe(df, hide_index=True, use_container_width=True)

# Some tips and reminders
st.markdown(
    """
    ### Here are a few tips and reminders as you fill in the template.\n
    1. Use the same time period for each item when recording the number
    of items sold.
    2. Include the cost of *each and every* ingredient used to prepare an item,
    including things like fryer oil, condiments, and garnishes.
    3. If ingredient costs or item prices changed during the time
    period you're analyzing, then use the most recent cost/price.
    """
)

### File downloader ###
file_downloader()
