from models.sentiment import get_sentiment


def gemini_reply(user_text):
    sentiment, polarity, scores = get_sentiment(user_text)

    text = user_text.lower()

    positive_words = ["love", "happy", "great", "amazing", "excellent", "good", "best", "enjoy", "awesome"]
    negative_words = ["sad", "bad", "hate", "worst", "angry", "terrible", "crash", "problem", "disappointed"]

    found_positive = [word for word in positive_words if word in text]
    found_negative = [word for word in negative_words if word in text]

    if sentiment == "Positive":
        emoji = "😊"
        emotion = "Happiness / Satisfaction / Appreciation"
        reason = "The sentence contains positive emotional signals."
        if found_positive:
            reason += f" Important words detected: {', '.join(found_positive)}."
        suggestion = "This tweet can be treated as positive feedback."
        summary = "The user is expressing a positive opinion."

    elif sentiment == "Negative":
        emoji = "😟"
        emotion = "Sadness / Anger / Dissatisfaction"
        reason = "The sentence contains negative emotional signals."
        if found_negative:
            reason += f" Important words detected: {', '.join(found_negative)}."
        suggestion = "This tweet may need attention, support, or improvement."
        summary = "The user is expressing a negative opinion."

    else:
        emoji = "😐"
        emotion = "Neutral / Informational"
        reason = "The sentence does not show strong positive or negative emotion."
        suggestion = "This tweet can be treated as neutral public opinion."
        summary = "The user is sharing a neutral or general statement."

    return f"""
{emoji} **Sentiment:** {sentiment}

📊 **Polarity Score:** `{polarity}`

🧠 **Emotion Detected:** {emotion}

📝 **Reason:** {reason}

📌 **VADER Scores:**  
Positive: `{scores["pos"]}`  
Negative: `{scores["neg"]}`  
Neutral: `{scores["neu"]}`  

💡 **Suggestion:** {suggestion}

✅ **Summary:** {summary}
"""