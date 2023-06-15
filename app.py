# import libraries
import streamlit as st
import pandas as pd
from file_functions import file_downloader, file_uploader

# app title
st.title('Welcome to Menuphi!')

st.markdown(
    """
        Kickstart your menu management journey with the ***Menuphi Custom Template***,
        your go-to tool for meticulously capturing crucial details about
        each and every mouthwatering item on your menu.
    """
    )

file_downloader()

st.markdown(
    """
    With the data on your menu items fully inputted, upload the
    template to Menuphi to unlock valuable insights through our ***Menu Engineering Analysis***.
    """
)

df = file_uploader()
st.dataframe(df)
