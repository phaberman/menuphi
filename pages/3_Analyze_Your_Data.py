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

tab1, tab2, tab3, tab4 = st.tabs(['Upload File', 'Menu Matrix', 'Analysis', 'Recommendations'])

# Upload file and display dataframe
with tab1:
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

# Show scatterplot
with tab2:
    st.markdown("Our *Menu Matrix* helps you quickly visualize your menu item performance.")
    if uploaded_file is not None:
        plot = plot_menu(df, 'Contribution Margin', 'Number Sold')
        st.plotly_chart(plot, use_container_width=True)

with tab3:
    st.markdown("Menuphi's analysis has categorized each of your menu items into one of these four categories.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('#### Stars :star:')
        if uploaded_file is not None:
            stars = df.loc[df['Category'] == 'Star']['Item Name'].tolist()
            st.markdown(f"*{', '.join(stars)}*")
    with col2:
        st.markdown('#### Plow-Horses :horse:')
        if uploaded_file is not None:
            plow_horses = df.loc[df['Category'] == 'Plow-Horse']['Item Name'].tolist()
            st.markdown(f"*{', '.join(plow_horses)}*")
    with col3:
        st.markdown('#### Puzzles :question:')
        if uploaded_file is not None:
            puzzles = df.loc[df['Category'] == 'Puzzle']['Item Name'].tolist()
            st.markdown(f"*{', '.join(puzzles)}*")
    with col4:
        st.markdown('#### Dogs :dog2:')
        if uploaded_file is not None:
            dogs = df.loc[df['Category'] == 'Dog']['Item Name'].tolist()
            st.markdown(f"*{', '.join(dogs)}*")

with tab4:
    st.markdown("Here are several recommendations based on our analysis of your menu items.")
    if uploaded_file is not None:
        if len(stars) == 1:
            st.markdown(f"1. Promote your *{', '.join(stars)}* and highlight it in your menu design.")
        elif len(stars) > 1:
            st.markdown(f"1. Promote your *{', '.join(stars[:-1])}* and *{', '.join(stars[-1:])}* and highlight them in you menu design.")
        else:
            st.markdown("There are no stars on your menu.")
        if len(plow_horses) == 1:
            st.markdown(f"2. Pair your *{', '.join(plow_horses)}* with high margin items or carefully alter the recipe to lower costs and increase margins.")
        elif len(plow_horses) > 1:
            st.markdown(f"2. Pair your *{', '.join(plow_horses[:-1])}* and *{', '.join(plow_horses[-1:])}* with high margin items and/or carefully alter the recipes to lower costs and increase margins.")
        else:
            st.markdown("There are no plow-horses on your menu.")
        if len(puzzles) == 1:
            st.markdown(f"3. Improve the menu description and placement of *{', '.join(puzzles)}* and have your staff recommend it to your customers.")
        elif len(puzzles) > 1:
            st.markdown(f"3. Improve the menu description and placement of *{', '.join(puzzles[:-1])}* and *{', '.join(puzzles[-1:])}* and have your staff recommend them to your customers.")
        else:
            st.markdown("There are no puzzles on your menu.")
        if len(dogs) == 1:
            st.markdown(f"4. Reinvent or rebrand your *{', '.join(dogs)}* or remove it from the menu altogether.")
        elif len(dogs) > 1:
            st.markdown(f"4. Reinvent or rebrand your *{', '.join(dogs[:-1])}* and *{', '.join(dogs[-1:])}* or remove them from the menu altogether.")
        else:
            st.markdown("There are no dogs on your menu.")
