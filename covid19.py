import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
st.set_page_config(page_title="covid 19", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6159-U.N.V RAVITEJA"]
st.title("Exploratory Data Analysis on covid 19  Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a covid 19 Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.title("covid 19 Data Analysis")



    # Display data
    if st.checkbox("Show data"):
        st.write(data.head())

    if st.checkbox("Describe cvid 19 Data"):
       st.write(data.describe())
    
   
    if st.checkbox("Show first 25 rows"):
        st.write(data.head(25))

    if st.checkbox("Show shape"):
        st.write(data.shape)

    if st.checkbox("Show index"):
        st.write(data.index)

    if st.checkbox("Show columns"):
        st.write(data.columns)

    #if st.checkbox("Show data types"):
        # Convert data types to strings as a workaround for Arrow bug
        #data = data.astype(str)
        #st.dataframe(data.dtypes)

    if st.checkbox("Show count of non-null values"):
        st.write(data.count())

    if st.checkbox("Show all Null Values"):
        st.write(data.isnull().sum())

    # Remove column with missing values
    if st.checkbox("Remove column with missing values"):
        data.drop(columns="country_name", inplace=True)
        st.write("Column 'country_name' removed.")

    

   # Create bar graph
    if st.checkbox("Show bar graph of total cases by country"):
        sns.barplot(data=data, x="date", y="total_cases")
        plt.xticks(rotation=90)
        st.pyplot()

    # Create line plot
    if st.checkbox("Show line plot of new deaths over time"):
        sns.lineplot(data=data, x="date", y="new_deaths")
        st.pyplot()
    # Create scatterplot
    if st.checkbox("Show scatterplot of total cases vs new deaths"):
        sns.scatterplot(data=data, x="total_cases", y="new_deaths")
        plt.xticks(rotation=90)
        st.pyplot()

    # Create interactive heatmap
    
    
    