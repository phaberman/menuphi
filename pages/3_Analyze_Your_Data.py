import streamlit as st
from functions import *
import pandas as pd
from pathlib import Path
import os

# Title
st.title('Analyze Your Data')

# st.divider()

# # Introduction

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(['Upload File', 'Analysis', 'Menu Matrix', 'Recommendations'])

# Upload file and display dataframe
with tab1:
    st.markdown('Once all of your menu item data in the template, upload it to **Menuphi** so we can work our magic!')
    uploaded_file = st.file_uploader('Choose a file', type='xlsx', label_visibility='hidden')
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
    # Table
        st.dataframe(df, hide_index=True, column_order=column_order, column_config=column_config, use_container_width=True)

# Analysis
with tab2:
    st.markdown("**Menuphi's** analysis has categorized each of your menu items into one of these four categories.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('#### Stars')
        st.markdown('Popularity :chart_with_upwards_trend: Profitablity :chart_with_upwards_trend:')
        with st.expander('View Stars'):
            if uploaded_file is not None:
                stars = df.loc[df['Category'] == 'Star']['Item Name'].tolist()
                st.markdown(f"*{', '.join(stars)}*")
    with col2:
        st.markdown('#### Plow-Horses')
        st.markdown('Popularity :chart_with_upwards_trend: Profitablity :chart_with_downwards_trend:')
        with st.expander('View Plow-Horses'):
            if uploaded_file is not None:
                plow_horses = df.loc[df['Category'] == 'Plow-Horse']['Item Name'].tolist()
                st.markdown(f"*{', '.join(plow_horses)}*")
    with col3:
        st.markdown('#### Puzzles')
        st.markdown('Popularity :chart_with_downwards_trend: Profitablity :chart_with_upwards_trend:')
        with st.expander('View Puzzles'):
            if uploaded_file is not None:
                puzzles = df.loc[df['Category'] == 'Puzzle']['Item Name'].tolist()
                st.markdown(f"*{', '.join(puzzles)}*")
    with col4:
        st.markdown('#### Dogs')
        st.markdown('Popularity :chart_with_downwards_trend: Profitablity :chart_with_downwards_trend:')
        with st.expander('View Dogs'):
            if uploaded_file is not None:
                dogs = df.loc[df['Category'] == 'Dog']['Item Name'].tolist()
                st.markdown(f"*{', '.join(dogs)}*")

# Show scatterplot
with tab3:
    st.markdown("Our *Menu Matrix* allows you to quickly visualize your menu item performance.")
    if uploaded_file is not None:
        plot = plot_menu(df, 'Contribution Margin', 'Number Sold')
        st.plotly_chart(plot, use_container_width=True)

# Recommendations
with tab4:
    st.markdown("Here are several recommendations based on our analysis of your menu items.")
    if uploaded_file is not None:
        recs(stars, plow_horses, puzzles, dogs)
