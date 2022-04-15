import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import os

@st.cache
def df_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

data_load_state = st.text('Loading data...')
df = df_from_csv(r"data\email_with_topic_sample_v2.csv")
data_load_state.text('Loading data...done!')

st.title("Enron Study Case.")
st.write(""" 
This webpage allow you to iterate in all available mails from Enron case.
""")
st.markdown("""---""") 
display = ("Company newsletter", 'Administrative arrangement', 'Investment strategy','Personnal conversations','Business and Strategy')
options = (0, 1, 2 , 3 , 4)
author = st.sidebar.selectbox('selct topic', options, format_func=lambda x: display[x])
# author =  st.sidebar.selectbox("Please select a specific topic", list(df["Dominant_Topic"].unique()))
df_author = df[df['Dominant_Topic'] == author]
# cluster = st.sidebar.selectbox("Main Topic",["0","1","2","3"])
cluster = st.sidebar.selectbox("Person of interest",list(df_author['x_origin'].unique()))
# cluster = st.selectbox()
df_clustered = df_author[df_author['x_origin'] == str(cluster)]
col1, col2 = st.columns(2)
col1.metric("Number of total emails", df_author.shape[0])
col2.metric(f"Number of email for {cluster}", df_clustered.shape[0])
st.markdown("""---""") 
# st.dataframe(df_clustered[['date','to','from','subject','body']])
email = st.sidebar.selectbox("Select an email to view more", list(df_clustered['subject']))
df_email = df_clustered[df_clustered['subject']==email]
df_email = df_email.reset_index()
# col3, col4, col5 = st.columns(3)
# col3.metric('Date', str(df_email['date']))
# col4.metric('From', str(df_email['from']))
# col5.metric('To', str(df_email['to']))
# with st.expander("Click to expand the email"):

st.write(df_email['body'][0])
