import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd

from sentiment.preprocess import clean_text
from sentiment.analyzer import get_sentiment

# ------------------------------
# 🧠 App Title & Description
# ------------------------------
st.title("📈 AI-Based Stock Market Sentiment Analyzer")

st.write(
    "Analyze public sentiment for any stock or company using live Twitter data and AI-powered sentiment analysis."
)

# ------------------------------
# 🧾 User Inputs
# ------------------------------
query = st.text_input("Enter Stock or Company Name", placeholder="e.g., TCS, Infosys, Reliance")
limit = st.slider("Number of Tweets to Analyze", min_value=10, max_value=200, value=50)
analyze_btn = st.button("🔍 Analyze Sentiment")

# ------------------------------
# 🔍 On Button Click: Analyze
# ------------------------------
if analyze_btn:
    if not query:
        st.warning("Please enter a company or stock name.")
    else:
        tweets = []
        st.info("⏳ Fetching tweets...")

        for tweet in sntwitter.TwitterSearchScraper(f"{query} since:2024-01-01").get_items():
            if len(tweets) >= limit:
                break
            tweets.append([tweet.date, tweet.content])

        if len(tweets) == 0:
            st.error("No tweets found. Try a different keyword.")
        else:
            df = pd.DataFrame(tweets, columns=["Date", "Tweet"])

            # ------------------------------
            # 🧹 Clean & Analyze Sentiment
            # ------------------------------
            df["Cleaned"] = df["Tweet"].apply(clean_text)
            df[["Sentiment", "Score"]] = df["Cleaned"].apply(lambda x: pd.Series(get_sentiment(x)))

            st.success(f"✅ Fetched and analyzed {len(df)} tweets about '{query}'")

            # ------------------------------
            # 📊 Sentiment Visualization
            # ------------------------------
            st.subheader("📊 Sentiment Distribution")
            st.bar_chart(df["Sentiment"].value_counts())