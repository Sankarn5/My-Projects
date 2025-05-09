from transformers import pipeline

# Load pre-trained BERT sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(message):
    result = sentiment_pipeline(message)[0]
    return result['label'], result['score']