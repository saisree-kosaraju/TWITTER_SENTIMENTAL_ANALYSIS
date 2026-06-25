import os
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

MODEL_PATH = "sentiment_model.pkl"

if os.path.exists(MODEL_PATH):
    ml_model = joblib.load(MODEL_PATH)
else:
    ml_model = None


def get_sentiment(text):
    text = str(text)

    scores = analyzer.polarity_scores(text)
    compound = round(scores["compound"], 4)

    if ml_model is not None:
        prediction = ml_model.predict([text])[0]

        if prediction == "Positive":
            sentiment = "Positive"
        elif prediction == "Negative":
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
    else:
        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

    return sentiment, compound, scores


def explain_sentiment(text):
    sentiment, compound, scores = get_sentiment(text)

    if sentiment == "Positive":
        emoji = "😊"
        emotion = "Happy / Satisfied"
        reason = "The text contains positive words or positive language patterns."
        suggestion = "This can be considered positive feedback."
    elif sentiment == "Negative":
        emoji = "😟"
        emotion = "Sad / Angry / Dissatisfied"
        reason = "The text contains negative words or complaint-like language patterns."
        suggestion = "This may need attention or support."
    else:
        emoji = "😐"
        emotion = "Neutral / Informational"
        reason = "The text does not show strong positive or negative emotion."
        suggestion = "This can be treated as neutral public opinion."

    return f"""
{emoji} **Sentiment:** {sentiment}

**Polarity Score:** `{compound}`

**Emotion:** {emotion}

**Reason:** {reason}

**VADER Scores:**  
Positive: `{scores["pos"]}`  
Negative: `{scores["neg"]}`  
Neutral: `{scores["neu"]}`  

**Suggestion:** {suggestion}
"""