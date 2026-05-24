import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

query = "SELECT * FROM news_sentiment"

df = pd.read_sql(query, engine)

st.title("News Sentiment Dashboard")

# st.dataframe(df)
def color_sentiment(val):
    if val > 0:
        return 'background-color: green; color: white'
    elif val < 0:
        return 'background-color: red; color: white'
    else:
        return 'background-color: grey; color: white'

styled_df = df.style.map(
    color_sentiment,
    subset=['sentiment_score']
)

st.dataframe(styled_df)

st.bar_chart(df["sentiment_score"])