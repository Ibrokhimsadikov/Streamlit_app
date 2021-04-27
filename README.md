# Streamlit_app
This is simple Streamlit ML app

 @st.cache(allow_output_mutation=True)
    def get_entity_options():
        entities = ["ENTITY", "ANATOMY", "DISORDERS", "OBS_DATE", "ASSERTION", "RESULT"]
        colors = {'ANATOMY': 'linear-gradient(180deg, #66ffcc, #abf763)', "OBS_DATE": "#e6ed80",'ENTITY': 'linear-gradient(90deg, #fc9ce7,#9cf6fc)', "DISORDERS":'linear-gradient(90deg, #ffff66, #ff6600)', "ASSERTION":'#8cfaef', "RESULT":"#f684fa"}
        options = {"ents": entities, "colors": colors}    
        return options
    options2 = get_entity_options()
    
    
    
    from negspacy.negation import Negex
    negex = Negex(nlp, language = "en_clinical_sensitive", chunk_prefix = ["no"])
        nlp.add_pipe(negex)


