import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import streamlit as st
import numpy as nps

# Import file
changping_df = pd.read_csv('.\data\PRSA_Data_Changping_20130301-20170228.csv')

# Adding a sidebar to select a year and month to view data
with st.sidebar:
    st.header('What date You Want to See?')
    st.markdown("\n")

    choosed_year = st.sidebar.selectbox('Choose Year', list(changping_df['year'].unique()))
    choosed_month = st.sidebar.selectbox('Choose Month', list(changping_df['month'].unique()))

# Filter data based on the selected year and month
data_filtered = changping_df[(changping_df['year'] == choosed_year) & (changping_df['month'] == choosed_month)].copy()

# Set the Title of Dashboard
st.title('Air Quality in Changping Station')

# Set the Description of Dashboard
st.write('This page provides an information about Air Quality in Changping especially inform the conditions of PM2.5 and the relations with other weather conditions since 2013')

# Data Statistic
st.subheader('Data Statistic for Air Quality')
st.write('This is data statistic of Air Quality in Changping Station')
st.write(data_filtered.describe())

# Seasonal Pattern of PM2.5
st.subheader('Seasonal Pattern of PM2.5 Levels')
seasonal_patterns = changping_df.groupby('month')['PM2.5'].mean()
#Plotting the Average Monthly of PM2.5
fig, ax = plt.subplots()
seasonal_patterns.plot(kind='bar', color='darkgrey', ax = ax)
plt.title('Average Monthly of PM2.5 Levels')
plt.xlabel('Month')
plt.ylabel('Average')
st.pyplot(fig)

st.write("How's the Patterns?")
st.write("""Seasonal trends in PM2.5 concentrations vary greatly depending on the region, 
        influenced by factors such as weather patterns and human actions. Some areas experience a 
        rise in PM2.5 during winter due to the increased use of wood-burning stoves and fireplaces for warmth. 
        Springtime can lead to changes as fluctuating weather conditions stir up dust and pollutants. 
        Many places see lower PM2.5 levels during the summer months, thanks to cleaner air and reduced indoor heating. 
        Autumn often witnesses a rise in PM2.5 as agricultural activities, such as crop burning, add to the particulate matter in the atmosphere. 
        It is essential to grasp these seasonal shifts for effective management of air quality and public health initiatives.  """
        )

st.markdown("\n")
st.markdown("\n")


# Correlation between air conditions
st.subheader('Correlation between Air Conditions')
select_item = st.multiselect('Choose the Condition', changping_df.columns, default=['PM2.5', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN'])
corr = changping_df[select_item].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)

st.write("What's the correlation?")
st.write(""" PM2.5 has a negative correlation with TEMPT and has a positive correlation with DEWP. Unexpected correlation 
         with PRESS and RAIN that has very small to no correlation. It means that PRESS and RAIN has no impact to PM2.5 concentrations."""
        )

# Adding feedback columns
text = st.text_area('Please sent us Your Feedback')
st.write('Feedback: ', text)

st.caption('Copyright © ichrvmnd 2024')



