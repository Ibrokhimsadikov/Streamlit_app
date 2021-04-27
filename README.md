# Streamlit_app
This is simple Streamlit ML app


    
    from negspacy.negation import Negex
    negex = Negex(nlp, language = "en_clinical_sensitive", chunk_prefix = ["no"])
        nlp.add_pipe(negex)


 for ent in linker(doc).ents:
            for ent_id, score in ent._.umls_ents:

                kb_entity = linker.umls.cui_to_entity[ent_id]

                tuis = ",".join(kb_entity.types)
                if kb_entity.types[0] in TUI.tui.values:
                    label=TUI[TUI['tui'] == kb_entity.types[0]].label.values[0]
                    value_extract= ' '.join([str(item) for item in ent._.value_extract])
                    data.append([
                        #text[0],
                        ent.text,
                        kb_entity.canonical_name,
                        #ent_id,
                        tuis,
                        #score,
                        label,
                        ent._.negex,
                        value_extract,
                        #kb_entity.aliases


                    ])


                if True:
                    break

