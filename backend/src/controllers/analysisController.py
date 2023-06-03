


import re
import spacy

class analysisClass:
    def analysisText(text):
        
        nlp = spacy.load("en_core_web_sm")
      
        doc = nlp(text)
       
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        
        dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
        
        entity_counts = {}
        for ent in doc.ents:
         
            if ent.label_ in entity_counts:
                entity_counts[ent.label_] += 1
            else:
                entity_counts[ent.label_] = 1
                   
        return {

                    'PERSON':entity_counts.get('PERSON', 0),

                    'GPE':entity_counts.get('GPE', 0),

                    'DATE':entity_counts.get('DATE', 0),

                    'WORK_OF_ART':entity_counts.get('WORK_OF_ART', 0)

                    }
            

        
        
