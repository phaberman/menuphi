import streamlit as st
from functions import file_uploader

# Title
st.title('Step 2: Upload Your Data')

# Introduction
st.markdown(
    """
    Now that you have all of your menu item data in the template,
    it's time to upload it to **Menuphi** so we can work our magic!\n
    Make sure that your template is saved as an *xlsx* file.\n
    If the upload was successful, you will see a preview of your data.
    """
)

### File uploader
df = file_uploader()

st.dataframe(df, hide_index=True, use_container_width=True)
