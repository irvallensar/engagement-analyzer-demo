import streamlit as st
import spacy
import spacy_streamlit

# 1. Set up the Streamlit page
st.title("Engagement Analyzer")
st.markdown("This tool uses a Data Augmented RoBERTa (DA-RoBERTa) model to identify and highlight engagement markers in academic text.")

# 2. Load your custom model (Streamlit caches this so it doesn't reload every time)
@st.cache_resource
def load_model():
    return spacy.load("model-best")

nlp = load_model()

# 3. Create the text input box for the user
default_text = "Though we do not advocate that researchers develop projects about issues in which they have little grounding, we do believe that researchers should view this disciplinary division as an opportunity rather than an obstacle."
user_text = st.text_area("Enter text to analyze:", default_text, height=200)

# 4. Process the text through DA-RoBERTa to create the 'doc'
doc = nlp(user_text)

# 5. Define your custom hex colors
custom_colors = {
    "MONOGLOSS": "#E0E0E0",     
    "ATTRIBUTION": "#B3E5FC",   
    "ENTERTAIN": "#C8E6C9",     
    "DENY": "#FFCDD2",          
    "COUNTER": "#FFE0B2",       
    "PROCLAIM": "#E1BEE7",      
    "SOURCES": "#D7CCC8",       
    "JUSTIFYING": "#FFF9C4",    
    "ENDOPHORIC": "#B2DFDB",    
    "CITATION": "#F5F5F5"       
}

# 6. Visualize the 'doc' with the custom colors
spacy_streamlit.visualize_ner(
    doc,
    labels=list(custom_colors.keys()),
    show_table=False, 
    title="Engagement Markers",
    displacy_options={"colors": custom_colors}
)
