import streamlit as st
import spacy
import spacy_streamlit

st.set_page_config(page_title="Academic Engagement Analyzer", layout="wide")

st.title("Academic Engagement Analyzer")
st.markdown("This tool uses a custom fine-tuned DA-RoBERTa model to identify and highlight pragmatic engagement markers in academic text.")

# Cache the model load so it doesn't crash the server memory!
@st.cache_resource
def load_model():
    return spacy.load("./model-best")

nlp = load_model()

# Create a text input box
default_text = "Smith (2022) introduces a novel approach to LLM prompting. However, this method obviously fails to account for syntax. We argue that further research is required."
user_input = st.text_area("Enter academic text to analyze:", default_text, height=150)

# The Engagement Labels
engagement_labels = ["ATTRIBUTION", "CITATION", "COUNTER", "DENY", "ENDOPHORIC", "ENTERTAIN", "JUSTIFYING", "MONOGLOSS", "PROCLAIM", "SOURCES"]

if st.button("Analyze Text"):
    if user_input:
        doc = nlp(user_input)
        
        # Built-in spaCy Streamlit visualizer!
        spacy_streamlit.visualize_ner(
            doc,
            labels=engagement_labels,
            show_table=False,
            title="Engagement Markers"
        )
