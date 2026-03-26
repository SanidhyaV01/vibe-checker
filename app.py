import streamlit as st
from transformers import pipeline

st.title("🧠 The Vibe Checker")
st.write("Enter any text below, and I'll use AI to tell you if it's **Positive** or **Negative**.")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")


with st.spinner("Loading AI Brain..."):
    classifier = load_model()

user_text = st.text_area("What's on your mind?",
                         placeholder="Type something like: 'I love coding with Python!'")

if st.button("Analyze Vibe"):
    if user_text.strip(): 
        result = classifier(user_text)
        
       
        label = result[0]['label']
        score = result[0]['score']
        
        if label == "POSITIVE":
            st.success(f"**Positive Vibe Detected!** (Confidence: {score:.2f})")
            st.balloons() 
        else:
            st.error(f"**Negative Vibe Detected.** (Confidence: {score:.2f})")
    else:
        st.warning("Please enter some text first!")
