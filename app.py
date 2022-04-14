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
df = df_from_csv(r"data/streamlit_df.csv")
data_load_state.text('Loading data...done!')

st.title("Enron Study Case.")
st.write(""" 
This webpage allow you to iterate in all available mails from Enron case.
""")
author =  st.sidebar.selectbox("Please select a person to investigate", list(df["x_origin"].unique()))
df_author = df[df['x_origin'] == author]
# cluster = st.sidebar.selectbox("Main Topic",["0","1","2","3"])
cluster = st.sidebar.selectbox("Main Topic",list(df_author['Dominant_Topic'].unique()))
# cluster = st.selectbox()
df_clustered = df_author[df_author['Dominant_Topic'] == int(cluster)]
col1, col2 = st.columns(2)
col1.metric("Number of total emails", df_author.shape[0])
col2.metric(f"Period email in {cluster} cluster", df_clustered.shape[0])
st.dataframe(df_clustered[['date','to','from','subject','body']])
email = st.sidebar.selectbox("Select an email to view more", list(df_clustered['subject']))
df_email = df_clustered[df_clustered['subject']==email]
col3, col4, col5 = st.columns(3)
col3.metric('Date', str(df_email['date']))
col4.metric('From', str(df_email['from']))
col5.metric('To', str(df_email['to']))
# with st.expander("Click to expand the email"):
st.text(df_email['body'].to_string())
