import numpy as np
import nltk
import pickle
import pandas as pd
import streamlit as st
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer

pickle_in = open("sentiment_model.pkl", "rb")
model = pickle.load(pickle_in)


# def preprocess_text(input_text):
#     port_stem = PorterStemmer()
#     stemmed_content = re.sub("[^a-zA-Z]", "", content)
#     stemmed_content = stemmed_content.lower()
#     stemmed_content = stemmed_content.split()
#     stemmed_content = [
#         port_stem.stem(word)
#         for word in stemmed_content
#         if not word in stopwords.words("english")
#     ]
#     stemmed_content = " ".join(stemmed_content)

#     return stemmed_content


def analyse_sentiment(transformed_text):
    sid = SentimentIntensityAnalyzer()

    sentiment_scores = sid.polarity_scores(transformed_text)

    if sentiment_scores.get("compound", 0) >= 0.6:
        sentiment = "Positive"
    elif sentiment_scores.get("compound", 0) <= 0.4:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(sentiment)
    return sentiment

    # prediction = model.predict(transformed_text)
    # print(prediction)
    # return prediction


def main():
    st.title("Sentiment Analyzer")
    st.markdown("Enter some text below to predict it's sentiment. :sparkles:")
    st.divider()

    text = st.text_input("text", help="Enter Text to be Analyzed")
    result = ""

    if st.button("Predict"):
        result = analyse_sentiment(text)

    st.divider()

    match result:
        case "Negative":
            with st.chat_message("user"):
                st.markdown("The sentiment is Negative :rage:")
        case "Positive":
            with st.chat_message("user"):
                st.markdown("The sentiment is Positive :blush:")
        case "Neutral":
            with st.chat_message("user"):
                st.markdown("The sentiment is Neutral :neutral_face:")
        case _:
            with st.chat_message("user"):
                st.markdown("Enter some text above to find the sentiment :sparkles:")


if __name__ == "__main__":
    main()
