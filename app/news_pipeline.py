import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Integra
API_KEY = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
articles = response.json()["articles"]

analyzer = SentimentIntensityAnalyzer()

data = []


for article in articles:
    title = article["title"]

    score = analyzer.polarity_scores(title)["compound"]

    data.append({
        "title": title,
        "description": article["description"],
        "sentiment": score,
        "source": article["source"]["name"]
    })

df = pd.DataFrame(data)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df.to_sql("news_sentiment", engine, if_exists="replace", index=False)

print("Data inserted successfully")