import streamlit as st
import pandas as pd
import numpy as np
import random
from pathlib import Path
import os

@st.cache
def df_from_csv(csv_file):
    df = pd.read_csv(csv_file).sample(5000)
    df['random'] = random.randint(0,3)
    return df

data_load_state = st.text('Loading data...')
st.text(os.path.abspath(''))
# path = Path(r"data\v3.csv")
df = df_from_csv(r"O:\Enron_Email_Dataset\data\v4.csv")
# df = pd.read_csv("data\v4.csv").sample(15000)
data_load_state.text('Loading data...done!')

st.title("Enron Study Case.")
st.write(""" 
This webpage allow you to iterate in all available mails from Enron case.
""")
author =  st.selectbox("Please select a person to investigate", list(df["x_origin"].unique()))
cluster = st.selectbox("Main Topic",["0","1","2","3"])
df_author = df[df['x_origin'] == author]
df_clustered = df_author[df_author['random'] == int(cluster)]
st.dataframe(df_clustered[['random','x_origin','body']])