# Libraries
# for file downloader
import streamlit as st
import xlsxwriter
from io import BytesIO
# for file uploader
import pandas as pd

### File downloader function ###
def file_downloader():
    output = BytesIO()

    # Write files to in-memory strings using BytesIO
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Define the column headers
    headers = ['Menu Category', 'Item Name', 'Item Price', 'Item Cost', 'Number Sold']

    # Define a format for bold headers
    bold_format = workbook.add_format({'bold': True})

    # Define a format for italicized cells
    italic_format = workbook.add_format({'italic': True})

    # Write the column headers to the worksheet in bold
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, bold_format)

    # Write the example values in the second row
    worksheet.write(1, 0, 'Burgers', italic_format)
    worksheet.write(1, 1, 'Classic Burger', italic_format)
    worksheet.write(1, 2, '8.99', italic_format)
    worksheet.write(1, 3, '3.25', italic_format)
    worksheet.write(1, 4, '40', italic_format)

    # Close and save the workbook
    workbook.close()

    # Download button
    return st.download_button(
        label='Download the template here',
        data=output.getvalue(),
        file_name='menu_data_template.xlsx',
        mime='application/vnd.ms-excel'
        # help="Don't forget to remove the example in row 1"
    )

### File uploader function ###
def file_uploader():
    uploaded_file = st.file_uploader('Choose a file', label_visibility='hidden')
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_excel(uploaded_file)
        return df
        # return st.dataframe(df, hide_index=True)
