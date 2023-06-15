import streamlit as st
import functions
import pandas as pd

# Title
st.title('Step 1: Download Our Template')

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

# Dataframe for example
data = {
    'Menu Category': ['Burgers'],
    'Item Name': ['Classic Burger'],
    'Menu Price': ['8.99'],
    'Cost': ['2.45'],
    'Number Sold': ['750']
}

df = pd.DataFrame(data)

st.dataframe(df, hide_index=True, use_container_width=True)
