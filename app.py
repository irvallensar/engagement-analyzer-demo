import streamlit as st
import spacy
import spacy_streamlit

st.set_page_config(page_title="Engagement Analyzer", layout="wide")

st.title("Engagement Analyzer")
st.markdown("This tool uses a Data Augmented RoBERTa (DA-RoBERTa) model to identify and highlight engagement markers in academic text.")

@st.cache_resource
def load_model():
    return spacy.load("./model-best")

nlp = load_model()

default_text = "It has been long proven that smokers not only harm themselves by smoking, but harm others around them too."
user_input = st.text_area("Enter text to analyze:", default_text, height=150)

engagement_labels = ["ATTRIBUTION", "CITATION", "COUNTER", "DENY", "ENDOPHORIC", "ENTERTAIN", "JUSTIFYING", "MONOGLOSS", "PROCLAIM", "SOURCES"]

if st.button("Analyze Text"):
    if user_input:
        doc = nlp(user_input)
        
        spacy_streamlit.visualize_ner(
            doc,
            labels=engagement_labels,
            show_table=False,
            title="Engagement Markers"
        )
