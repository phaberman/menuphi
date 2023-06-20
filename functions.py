# Libraries
# for file downloader
import streamlit as st
import xlsxwriter
from io import BytesIO
# for file uploader
import pandas as pd
# for plotly chart
import plotly.express as px

### Page configurations ###
def page_configs():
    st.set_page_config(layout='wide')

### File downloader function ###
def file_downloader():
    output = BytesIO()

    # Write files to in-memory strings using BytesIO
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    # Define the column headers
    headers = ['Menu Category', 'Item Name', 'Menu Price', 'Cost', 'Number Sold']

    # Define a format for bold headers
    bold_format = workbook.add_format({'bold': True})

    # Write the column headers to the worksheet in bold
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, bold_format)

    # Close and save the workbook
    workbook.close()

    # Download button
    return st.download_button(
        label='Click to Download',
        data=output.getvalue(),
        file_name='menu_data_template.xlsx',
        mime='application/vnd.ms-excel'
    )

### File uploader function ###
def file_uploader():
    uploaded_file = st.file_uploader('Choose a file', type='xlsx', label_visibility='hidden', )
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_excel(uploaded_file)

        # Add a'Contribution Margin' Column
        df['Contribution Margin'] = df['Menu Price'] - df['Cost']

        # Calculate the mean of 'contribution margin' column
        contribution_mean = df['Contribution Margin'].mean()

        # Calculate the mean of 'number sold' column
        sold_mean = df['Number Sold'].mean()

        # Create a function to apply the conditions and assign the appropriate category
        def assign_category(row):
            if row['Contribution Margin'] >= contribution_mean and row['Number Sold'] >= sold_mean:
                return 'Star'
            elif row['Contribution Margin'] < contribution_mean and row['Number Sold'] >= sold_mean:
                return 'Plow-Horse'
            elif row['Contribution Margin'] >= contribution_mean and row['Number Sold'] < sold_mean:
                return 'Puzzle'
            else:
                return 'Dog'

        # Apply the function to create the 'Category' column
        df['Category'] = df.apply(assign_category, axis=1)

        return df


### TO DATAFRAME
def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)

    # Add a'Contribution Margin' Column
    df['Contribution Margin'] = df['Menu Price'] - df['Cost']

    # Calculate the mean of 'contribution margin' column
    contribution_mean = df['Contribution Margin'].mean()

    # Calculate the mean of 'number sold' column
    sold_mean = df['Number Sold'].mean()

    # Create a function to apply the conditions and assign the appropriate category
    def assign_category(row):
        if row['Contribution Margin'] >= contribution_mean and row['Number Sold'] >= sold_mean:
            return 'Star'
        elif row['Contribution Margin'] < contribution_mean and row['Number Sold'] >= sold_mean:
            return 'Plow-Horse'
        elif row['Contribution Margin'] >= contribution_mean and row['Number Sold'] < sold_mean:
            return 'Puzzle'
        else:
            return 'Dog'

    # Apply the function to create the 'Category' column
    df['Category'] = df.apply(assign_category, axis=1)

    return df




### Ploty Scatter Plot ###

import plotly.express as px

def plot_menu(df, profit_col, popularity_col):
    profitability_threshold = df[profit_col].mean()
    popularity_threshold = df[popularity_col].mean()

    # Assign labels based on profitability and popularity categories
    df['label'] = ''
    df.loc[(df[profit_col] >= profitability_threshold) & (df[popularity_col] >= popularity_threshold), 'label'] = 'Star'
    df.loc[(df[profit_col] >= profitability_threshold) & (df[popularity_col] < popularity_threshold), 'label'] = 'Puzzle'
    df.loc[(df[profit_col] < profitability_threshold) & (df[popularity_col] >= popularity_threshold), 'label'] = 'Plow-Horse'
    df.loc[(df[profit_col] < profitability_threshold) & (df[popularity_col] < popularity_threshold), 'label'] = 'Dog'

    # Abbreviate data point text labels
    # df['abbreviated_menu_item'] = df['menu_item'].str[:5] + '...'

    # Create a scatter plot using Plotly Express
    fig = px.scatter(df, x=profit_col, y=popularity_col, color='label', text=df['Item Name'].str[:5] + '...', size_max=10)

    # Customize the plot appearance
    fig.update_traces(
        textfont=dict(color='black', size=12),  # Increase the font size
        hovertemplate='<b>%{text}</b>',
        textposition='bottom center'  # Position the text labels at the bottom center
    )
    fig.update_layout(
        title='Profitability vs. Popularity',
        xaxis_title='Profitability',
        yaxis_title='Popularity',
        width=800,
        height=500,
        template='plotly_white',  # Use a simple white template
        font_family='Arial',
        font_color='black',
        legend=dict(
            orientation='h',
            yanchor='top',
            y=1.1,  # Adjust the position
            xanchor='center',
            x=0.5,
            itemclick=False,
            title=None  # Remove the legend title
        ),
        margin=dict(t=80, b=50, l=50, r=50),
        xaxis=dict(
            zeroline=True,  # Show the x-axis line
            zerolinecolor='gray',  # Set the color of the x-axis line
            zerolinewidth=1,  # Set the width of the x-axis line
            showgrid=False  # Remove the x-axis gridlines
        ),
        yaxis=dict(
            zeroline=True,  # Show the y-axis line
            zerolinecolor='gray',  # Set the color of the y-axis line
            zerolinewidth=1,  # Set the width of the y-axis line
            showgrid=False  # Remove the y-axis gridlines
        ),
        shapes=[
            dict(
                type="line",
                x0=min(df[profit_col]),
                y0=df[popularity_col].mean(),
                x1=max(df[profit_col]),
                y1=df[popularity_col].mean(),
                line=dict(color='gray', width=1),
                opacity=0.3,
                layer='below'
            ),
            dict(
                type="line",
                x0=df[profit_col].mean(),
                y0=min(df[popularity_col]),
                x1=df[profit_col].mean(),
                y1=max(df[popularity_col]),
                line=dict(color='gray', width=1),
                opacity=0.3,
                layer='below'
            )
        ]
    )

    # Show the plot
    return fig

### TABLE PLOT
