#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import streamlit as st
# import spacy
# from spacy import displacy
# import pandas as pd

# from scispacy.umls_linking import UmlsEntityLinker
# from scispacy.abbreviation import AbbreviationDetector



import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
import spacy
from spacy import displacy
import pandas as pd

from scispacy.umls_linking import UmlsEntityLinker
from scispacy.abbreviation import AbbreviationDetector



@st.cache(allow_output_mutation=True)
def load_model():

    nlp = spacy.load("en_core_sci_lg")
    # Add abbreviation detector
    abbreviation_pipe = AbbreviationDetector(nlp)
    nlp.add_pipe(abbreviation_pipe)
    return nlp

@st.cache(allow_output_mutation=True)
def process_text(text):
    nlp = load_model("en_core_sci_lg")
    return nlp(text)

@st.cache(allow_output_mutation=True)
def load_linker():
    linker = UmlsEntityLinker(resolve_abbreviations=True)

    return linker


DEFAULT_TEXT = "Spinal and bulbar muscular atrophy (SBMA) is an inherited motor neuron disease caused by the expansion of a polyglutamine tract within the androgen receptor (AR). SBMA can be caused by this easily."
def main():
    st.title("File Upload Tutorial")
    

    menu = ["Text Input","Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)
    model_load_state = st.info(f"Loading model...")
    nlp = load_model()
    model_load_state.empty()

    linker = load_linker()

    st.sidebar.header("Entity Linking")
    threshold = st.sidebar.slider("Mention Threshold", 0.0, 1.0, 0.85)
    linker.threshold = threshold
    show_only_top = st.sidebar.checkbox("Show only top entity per mention", value=True)

    if choice == "Text Input":
        st.subheader("Home")
        st.header("Enter some text:")
        text = st.text_area("", DEFAULT_TEXT)



    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if st.button("Process"):
            if data_file is not None:
                df = pd.read_csv(data_file)
                #st.dataframe(df)
                st.sidebar.subheader("Dataset Attributes")
                st.sidebar.selectbox("Choose Column",df.columns)
                row_selection = st.sidebar.number_input('Select desired record:', min_value=0, max_value=99998, value=0,step=1)
    nlp = load_model(spacy_model)            
    st.sidebar.header("Entity Mapping")
    threshold = st.sidebar.slider("Mention Threshold", 0.0, 1.0, 0.85)
    linker.threshold = threshold
    show_only_top = st.sidebar.checkbox("Show only top entity per mention", value=True)





if __name__ == '__main__':
    main()
