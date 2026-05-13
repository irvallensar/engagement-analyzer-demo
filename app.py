import streamlit as st
import spacy
import spacy_streamlit

# 1. Set up the Streamlit page
st.title("Engagement Analyzer")
st.markdown("This tool uses a Data Augmented RoBERTa (DA-RoBERTa) model to identify and highlight engagement markers in academic text.")

# 2. Load custom model
@st.cache_resource
def load_model():
    return spacy.load("model-best")

nlp = load_model()

# 3. Create the text input box for the user
default_text = "A designated smoking area is required to smoke not just in restaurants but even in hawker and shopping cents . Smokers , on the other hand , think that this is against their rights and freedom . In my opinion , however , smoking should be completely banned at all restaurants ."
user_text = st.text_area("Enter text to analyze:", default_text, height=200)

# 4. Create Analyze Text button
if st.button("Analyze Text"):
    
    # 5. Process the text through DA-RoBERTa ONLY when the button is clicked
    doc = nlp(user_text)

    # 6. Define custom hex colors
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

    # 7. Visualize the 'doc' with the custom colors
    spacy_streamlit.visualize_ner(
        doc,
        labels=list(custom_colors.keys()),
        show_table=False, 
        title="Engagement Markers",
        displacy_options={"colors": custom_colors}
    )
