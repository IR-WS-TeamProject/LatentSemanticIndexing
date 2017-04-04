"""
    This module can compute the list of ranked documents given the svd, the query and the documents
"""

import numpy as np

### Temporary Mock data ####################################################

MOCK_DOCS = [
    'rec.sport.baseball/100521',
    'rec.sport.baseball/101666',
    'rec.sport.baseball/102151',
    'sci.med/57110', 'sci.med/58047'
]
# ['data/20news-bydate/20news-bydate-train/rec.sport.baseball/100521']
MOCK_TERM_VECTOR = np.mat([1, 0, 0, 2]).T
MOCK_SK = np.mat([[4, 0], [0, 1]])
MOCK_UK = np.mat([[0.5, 0.4], [0.1, 0.2], [0.25, 0.05], [0.15, 0.35]])
MOCK_VK_TRANSPOSED = np.mat([[0.2, 0.1, 0.3, 0.4, 0.0], [0.1, 0.3, 0.2, 0.1, 0.3]])
MOCK_COS = np.mat([[0.15, 0.35, 0.28, 0.19, 0.33]])

############################################################################

def get_term_vector(query=''):
    """TODO function should be provided within the preprocessing process"""
    print('Query is not yet used: ', query)
    return MOCK_TERM_VECTOR

def unitify_vector(vector):
    """return unit length vector"""
    return vector / vector.sum()

def map_vector_to_lower_rank(termvector, s_k=MOCK_SK, u_k=MOCK_UK):
    """map a termvector in the k-dimensional space"""
    sk_inverse = s_k.I
    uk_transposed = u_k.T
    return sk_inverse * uk_transposed * termvector

def compute_cosine_similarities(termvector_k, v_k_transposed=MOCK_VK_TRANSPOSED):
    """
        Compute the cosine similarity between a k-rank termvector and the k-rank v matrix.
        Result: vector with a similarity between the termvector and each document.
    """
    dk_unit = unitify_vector(termvector_k)
    return dk_unit.T * v_k_transposed

def compute_ranked_list(cosine_vector=MOCK_COS, docs=None):
    """returns the list of ranked docs"""
    if docs is None:
        docs = MOCK_DOCS

    if cosine_vector.shape[1] != len(docs):
        return []

    ranked_docs = []
    for i in range(0, cosine_vector.shape[1]):
        ranked_docs.append({'doc': docs[i], 'rank': cosine_vector[0, i]})

    ranked_docs.sort(key=lambda obj: obj['rank'], reverse=True)
    return ranked_docs

def get_ranked_list(query, docs, u_k, s_k, v_k_transposed):
    """Core function of this module: Get a list of ranked documents"""
    termvector = get_term_vector(query)
    termvector_k = map_vector_to_lower_rank(termvector, s_k, u_k)
    cosine_vector = compute_cosine_similarities(termvector_k, v_k_transposed)
    return compute_ranked_list(cosine_vector, docs)

def get_ranked_list_mock():
    """Get list of ranked mock documents with a mocked query"""
    termvector = get_term_vector('')
    termvector_k = map_vector_to_lower_rank(termvector, MOCK_SK, MOCK_UK)
    cosine_vector = compute_cosine_similarities(termvector_k, MOCK_VK_TRANSPOSED)
    return compute_ranked_list(cosine_vector, MOCK_DOCS)
