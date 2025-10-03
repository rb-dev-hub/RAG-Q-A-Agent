from src.similarity import calculate_similarity
import numpy as np
from src.embeddings import get_embedding

def get_context(prompt, chunks_from_file):
    embedding_prompt = get_embedding(prompt)
    embedding_prompt_array = np.array(embedding_prompt)

    embedding_file_list = []
    for chunk in chunks_from_file:
        vec_chunk = get_embedding(chunk)
        embedding_file_list.append(vec_chunk)

    embedding_file_array = np.array(embedding_file_list)
    cosine_values = calculate_similarity(embedding_file_array, embedding_prompt_array)
    cosine_tuple = zip(cosine_values, chunks_from_file)

    sorted_tuple=sorted(cosine_tuple, reverse=True)
    relevant_chunks_list = [chunks_from_file for cosine_values, chunks_from_file in sorted_tuple[:2]]
    context = " ".join(relevant_chunks_list)
    return context


