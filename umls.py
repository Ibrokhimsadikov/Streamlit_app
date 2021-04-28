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
#from negspacy.negation import Negex
from spacy import displacy
import pandas as pd

from scispacy.umls_linking import UmlsEntityLinker
from scispacy.abbreviation import AbbreviationDetector

#####TUIs
TUI=pd.read_csv("tui_best.csv")
#TUI = TUI[TUI['label'].isin(label_list)].reset_index(drop=True)

@st.cache(allow_output_mutation=True)
def load_model():

    nlp = spacy.load("en_core_sci_lg")
    # Add abbreviation detector
    abbreviation_pipe = AbbreviationDetector(nlp)
    nlp.add_pipe(abbreviation_pipe)
    return nlp



@st.cache(allow_output_mutation=True)
def load_linker():
    linker = UmlsEntityLinker(resolve_abbreviations=True)

    return linker


@st.cache(allow_output_mutation=True)
def get_entity_options():
    entities = ["ENTITY", "ANATOMY", "DISORDERS", "OBS_DATE", "ASSERTION", "RESULT"]
    colors = {'ANATOMY': 'linear-gradient(180deg, #66ffcc, #abf763)', "OBS_DATE": "#e6ed80",'ENTITY': 'linear-gradient(90deg, #fc9ce7,#9cf6fc)', "DISORDERS":'linear-gradient(90deg, #ffff66, #ff6600)', "ASSERTION":'#8cfaef', "RESULT":"#f684fa"}
    options = {"ents": entities, "colors": colors}    
    return options
options2 = get_entity_options()


DEFAULT_TEXT = "Spinal and bulbar muscular atrophy (SBMA) is an inherited motor neuron disease caused by the expansion of a polyglutamine tract within the androgen receptor (AR). SBMA can be caused by this easily."
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""


def main():
    
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 1150px;
        padding-top: 5rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 10rem;
    }}
    .reportview-container .main {{
        color: "#fff";
        background-color: #fff;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

    
    
    st.title("Cognitive Entity Mapping ")
    st.subheader("Via pre-trained SciSpacy model")
    

    menu = ["Text Input","Dataset"]
    choice = st.sidebar.selectbox("Menu",menu)
    model_load_state = st.info(f"Loading model...")
    nlp = load_model()
    model_load_state.empty()

    linker = load_linker()

    st.sidebar.header("Mapping Attributes")
    threshold = st.sidebar.slider("Mention Threshold", 0.0, 1.0, 0.85)
    linker.threshold = threshold
    show_only_top = st.sidebar.checkbox("Show only top entity per mention", value=True)

    if choice == "Text Input":
        
        st.subheader("Enter some text:")
        text = st.text_area("", DEFAULT_TEXT)
        doc=nlp(text)
        if doc:
            st.header("Entity Linking")
            st.markdown("Mentions are detected with the standard pipeline's mention detector.")


            html = displacy.render(doc, style="ent", options=options2)
            # Newlines seem to mess with the rendering
            html = html.replace("\n", " ")
            st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)


            data = []
            for ent in linker(doc).ents:
                for ent_id, score in ent._.umls_ents:

                    kb_entity = linker.umls.cui_to_entity[ent_id]
                    tuis = ",".join(kb_entity.types)
                    label=TUI[TUI['tui'] == kb_entity.types[0]].label.values[0]
                    data.append([
                        ent.text,
                        kb_entity.canonical_name,
                        ent_id,
                        tuis,
                        label,
                        score,

                    ])

                    if show_only_top:
                        break

            attrs = ["Entity text", "UMLS Name", "Concept ID", "TUI(s)", "Label", "Similarity Score"]
            df = pd.DataFrame(data, columns=attrs)
            dfStyler = df.style.set_properties(**{'text-align': 'center'})
            dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])

            st.markdown("Entities are mapped to the Unified Medical Language System (UMLS).")
            st.table(dfStyler)
        



    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV",type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            
            st.sidebar.subheader("Dataset Attributes")   
            column=st.sidebar.selectbox("Choose Column",df.columns)
            row_selection = st.sidebar.number_input('Select desired record:', min_value=0, max_value=99998, value=0,step=1)
            if row_selection:
                subset=df[column][row_selection]
                doc=nlp(subset)
                if doc:
                    st.header("Entity Linking")
                    st.markdown("Mentions are detected with the standard pipeline's mention detector.")


                    html = displacy.render(doc, style="ent", options=options2)
                    # Newlines seem to mess with the rendering
                    html = html.replace("\n", " ")
                    st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)


                    data = []
                    for ent in linker(doc).ents:
                        for ent_id, score in ent._.umls_ents:

                            kb_entity = linker.umls.cui_to_entity[ent_id]
                            tuis = ",".join(kb_entity.types)
                            label=TUI[TUI['tui'] == kb_entity.types[0]].label.values[0]
                            data.append([
                                ent.text,
                                kb_entity.canonical_name,
                                ent_id,
                                tuis,
                                label,
                                score,

                            ])

                            if show_only_top:
                                break

                    attrs = ["Entity text", "UMLS Name", "Concept ID", "TUI(s)", "Label", "Similarity Score"]
                    df = pd.DataFrame(data, columns=attrs)
                    dfStyler = df.style.set_properties(**{'text-align': 'center'})
                    dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])

                    st.markdown("Entities are mapped to the Unified Medical Language System (UMLS).")
                    st.table(dfStyler)
                    
    st.sidebar.text("")  
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")  
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.header("Acknowledgements")
    st.sidebar.markdown(
        """
    Adapted from [Ines Montani]'s brilliant [spaCy](https://spacy.io), Mark Neumann and Daniel King  to work with Scispacy     [Allen AI](https://allenai.org/).
    """
    )  
                
                
    
    
                   

        
        
        
    
        
    
    




if __name__ == '__main__':
    main()