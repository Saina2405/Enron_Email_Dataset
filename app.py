import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Enron email cluster",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)


@st.cache
def df_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df


data_load_state = st.text("Loading data...")
df = df_from_csv(r"data/email_with_topic_sample_v2.csv")
data_load_state.text("Loading data...done!")

st.title("Enron Study Case.")
st.write(
    """
This webpage allow you to iterate in all available mails from Enron case.
"""
)
st.markdown("""---""")
display = (
    "Company newsletter",
    "Administrative arrangement",
    "Investment strategy",
    "Personal conversations",
    "Business and Strategy",
)
options = (0, 1, 2, 3, 4)
author = st.sidebar.selectbox(
    "Please select a specific topic", options, format_func=lambda x: display[x]
)

df_author = df[df["Dominant_Topic"] == author]

cluster = st.sidebar.selectbox(
    "Person of interest", list(df_author["x_origin"].unique())
)

df_clustered = df_author[df_author["x_origin"] == str(cluster)]
col1, col2 = st.columns(2)
col1.metric("Number of total emails", df_author.shape[0])
col2.metric(f"Number of email for {cluster}", df_clustered.shape[0])
st.markdown("""---""")

email = st.sidebar.selectbox(
    "Select an email to view more", list(df_clustered["subject"])
)
df_email = df_clustered[df_clustered["subject"] == email]
df_email = df_email.reset_index()

st.write(df_email["body"][0])
