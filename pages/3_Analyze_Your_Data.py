import streamlit as st
from functions import *
import pandas as pd
from pathlib import Path
import os

# Title
st.title('Analyze Your Data')

st.divider()

# Introduction
st.markdown(
    """
    Once all of your menu item data in the template,
    upload it to **Menuphi** so we can work our magic!
    """
)

# Upload file
uploaded_file = st.file_uploader('Choose a file', type='xlsx', label_visibility='hidden')

### Transform and display dataframe ###
if uploaded_file is not None:
    df = load_data(uploaded_file)
    column_order=[
        'Menu Category', 'Item Name', 'Menu Price',
        'Cost', 'Contribution Margin', 'Number Sold', 'Category'
        ]
    column_config={
        'Menu Price': st.column_config.NumberColumn(format='$%.2f'),
        'Cost': st.column_config.NumberColumn(format='$%.2f'),
        'Contribution Margin': st.column_config.NumberColumn(format='$%.2f')
        }
    st.dataframe(df, hide_index=True, column_order=column_order, column_config=column_config, use_container_width=True)

st.divider()

# Plot
plot = plot_menu(df, 'Contribution Margin', 'Number Sold')

st.plotly_chart(plot, use_container_width=True)

# Table
stars = []
plow_horses = []
puzzles = []
dogs = []

for index, row in df.iterrows():
    if row['Category'] == 'Star':
        stars.append(row['Item Name'])
    elif row['Category'] == 'Plow-Horse':
        plow_horses.append(row['Item Name'])
    elif row['Category'] == 'Puzzle':
        puzzles.append(row['Item Name'])
    elif row['Category'] == 'Dog':
        dogs.append(row['Item Name'])
