import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


class relevanceClass:
    # функция  relevance принимает запрос и текст из сайта, и вычислят релевантности 
    
    @staticmethod
    def relevance(query:str,data:str)->float:
        df = pd.DataFrame([data], columns = ['text'])
        text = df['text']
        encoder = SentenceTransformer("paraphrase-mpnet-base-v2")
        vectors = encoder.encode(text)
        vector_dimension = vectors.shape[1]
        index = faiss.IndexFlatL2(vector_dimension)
        faiss.normalize_L2(vectors)
        index.add(vectors)
        search_vector = encoder.encode(query)
        _vector = np.array([search_vector])
        faiss.normalize_L2(_vector)

        k = index.ntotal
        distances, ann = index.search(_vector, k=k)
        
        return float(distances[0][0])