# import libraries
import streamlit as st
import pandas as pd

# app title
st.title('Welcome to Menuphi!')

# load data
df = pd.read_excel('data/menu_data.xlsx')

# format dataframe
format_dict = {'Cost': '${:.2f}', 'Price': '${:.2f}', 'Contribution Margin': '${:.2f}'}

# display dataframe
st.dataframe(df.style.format(format_dict), hide_index=True)
