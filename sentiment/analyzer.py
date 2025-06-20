from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'Positive', score['compound']
    elif score['compound'] <= -0.05:
        return 'Negative', score['compound']
    else:
        return 'Neutral', score['compound']
