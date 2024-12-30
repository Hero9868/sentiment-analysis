import numpy as np
import pickle
import pandas as pd
import streamlit as st
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

pickle_in = open("sentiment_model.pkl", "rb")
model = pickle.load(pickle_in)


def preprocess_text(input_text):
    port_stem = PorterStemmer()
    stemmed_content = re.sub("[^a-zA-Z]", "", content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [
        port_stem.stem(word)
        for word in stemmed_content
        if not word in stopwords.words("english")
    ]
    stemmed_content = " ".join(stemmed_content)

    return stemmed_content


def analyse_sentiment(transformed_text):
    prediction = model.predict(transformed_text)
    print(prediction)
    return prediction


def main():
    st.title("Sentiment Analyzer")
    st.markdown("Enter some text below to predict it's sentiment. :sparkles:")
    st.divider()

    text = st.text_input("text", "Type Here")
    result = ""

    if st.button("Predict"):
        result = analyse_sentiment(text)
