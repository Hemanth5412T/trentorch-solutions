import numpy as np


def retrieval_cosine_gate(query: np.ndarray, documents: np.ndarray) -> np.ndarray:
    """
    query: array of shape (d,).
    documents: array of shape (n, d).

    Returns an array of shape (n,): cosine similarity between query and
    each document row. If either the query or a document has zero norm,
    that document's similarity is 0.
    """
    # TODO: compute dot(query, doc) / (||query|| * ||doc||) per document,
    # guarding against zero norms.
    lst = []
    for doc in documents:
        if not ((np.linalg.norm(query))*(np.linalg.norm(doc))):
            lst.append(0)
        else:
            s_i = np.dot(query,doc)/((np.linalg.norm(query))*(np.linalg.norm(doc)))
            lst.append(s_i)
        
    return np.array(lst)
