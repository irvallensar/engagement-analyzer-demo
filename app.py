import streamlit as st
import spacy
import spacy_streamlit

custom_colors = {
    "MONOGLOSS": "#E0E0E0",     # Light Grey
    "ATTRIBUTION": "#B3E5FC",   # Light Blue
    "ENTERTAIN": "#C8E6C9",     # Light Green
    
    "DENY": "#FFCDD2",          # Light Red
    "COUNTER": "#FFE0B2",       # Light Orange
    "PROCLAIM": "#E1BEE7",      # Light Purple
    
    "SOURCES": "#D7CCC8",       # Light Brown
    "JUSTIFYING": "#FFF9C4",    # Light Yellow
    "ENDOPHORIC": "#B2DFDB",    # Light Teal
    "CITATION": "#F5F5F5"       # Off-White
}

spacy_streamlit.visualize_ner(
    doc,
    labels=list(custom_colors.keys()),
    show_table=False, # Set to True if you want the table view beneath it
    title="Engagement Markers",
    displacy_options={"colors": custom_colors}
)

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
