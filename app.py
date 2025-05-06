import streamlit as st
from textblob import TextBlob

st.tittle("Simple Sentiment Analysis")

text = st.text_areal(" Enter a Sentence or review: ")
if st.button(" Analyze "):
    blob = TextBlob(text)
    polarity = blob.sentiment. polarity

    if polarity > 0 :
        st.success("Sentiment: Positive 😁")
    elif polarity < 0:
        st.error("Sentiment: Negative 😌 ")
    else:
        st.info("Sentiment: Neutral  😑 ")