import streamlit as st
from functions import file_uploader, plot_menu
import pandas as pd
from pathlib import Path

# Title
st.title('Step 2 and 3: Upload and Analyze Your Data')

st.divider()

# Introduction
st.markdown(
    """
    Now that you have all of your menu item data in the template,
    it's time to upload it to **Menuphi** so we can work our magic!
    """
)

### File uploader
df = file_uploader()

st.markdown(
    """
    If the upload was successful,
    you'll see a preview of your data below.
    """
)

### Display Data ###

# Configure columns
column_config = {
    'Menu Price': st.column_config.NumberColumn(format='$%.2f'),
    'Cost': st.column_config.NumberColumn(format='$%.2f'),
    'Contribution Margin': st.column_config.NumberColumn(format='$%.2f')
}

# Column order
column_order = [
    'Menu Category', 'Item Name', 'Menu Price',
    'Cost', 'Contribution Margin', 'Number Sold', 'Category'
    ]

# Display dataframe
st.dataframe(df, hide_index=True, use_container_width=True, column_config=column_config, column_order=column_order)

# Plot
plot = plot_menu(df, 'Contribution Margin', 'Number Sold')

st.plotly_chart(plot, use_container_width=True)
