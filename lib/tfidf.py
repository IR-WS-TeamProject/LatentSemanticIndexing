import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import svds
import json

#Input: Dict or filepath to json encoded dict
#returns TFIDF COO-Matrix and sorted Vocabulary + IDF-Vector
def createTFIDFMatrix(docs):
    #Handle finput formats (target: dict)
    if not isinstance(docs,dict):
        if isinstance(docs, str):
            with open(docs, 'r') as infile:
                docs = json.load(infile)
        else:
            print("TF-IDF: Unsupported format of documents as input!")
            return

    # Based on: https://datascience.blog.wzb.eu/2016/06/17/creating-a-sparse-document-term-matrix-for-topic-modeling-via-lda/
    # -> adapted to fit TermxDoc Matrix without additional transpose at the end

    # Init Vocabulary (Set)
    vocab = set()

    # Init Count of Non-Zero Values
    n_nonzero = 0

    # Iterate over documents an create vocabulary
    for docterms in docs.values():
        unique_terms = set(docterms)  # all unique terms of this doc (set of terms)
        vocab |= unique_terms  # set union: add unique terms of this doc
        n_nonzero += len(unique_terms)  # increase Non-Zero count by adding count of unique terms in this doc

    # convert to numpy for processing
    docpaths = np.array(list(
        docs.keys()))  # keys of dictionary (order of dictionary is used, but this doesn't correspond to order of inserts!)
    vocab = np.array(list(vocab))

    # Array containing sorted indices
    vocab_sorter = np.argsort(vocab)

    # print(vocab_sorter) #sorted indizes
    # print(vocab[vocab_sorter]) #outputs sorted vocabulary

    ndocs = len(docpaths)
    nvocab = len(vocab)

    # Initialize components of COO-Matrix (values, row indizes, col indizes) with emtpy values (for all non-zero elements)
    data = np.empty(n_nonzero, dtype=np.float32)  # all non-zero term frequencies at data[i,k]
    rows = np.empty(n_nonzero, dtype=np.intc)  # row index for [i,k]th data item (ith term freq.)
    cols = np.empty(n_nonzero, dtype=np.intc)  # column index for [i,k]th data item (kth document)

    # Init index (w.r.t. position in arrays of sparse COO matrix)
    ind = 0
    global_indices = []
    # go through all documents with their terms
    for docpath, terms in docs.items():
        # find indices into  such that, if the corresponding elements in  were
        # inserted before the indices, the order of  would be preserved
        # -> array of indices of  in
        term_indices = vocab_sorter[np.searchsorted(vocab, terms, sorter=vocab_sorter)]

        # count the unique terms of the document and get their vocabulary indices
        uniq_indices, counts = np.unique(term_indices, return_counts=True)

        # add (unique) indices of current doc to a list which is later on used for df
        global_indices.extend(uniq_indices)

        n_vals = len(uniq_indices)  # = number of unique terms
        ind_end = ind + n_vals  # to  is the slice that we will fill with data

        data[ind:ind_end] = counts  # save the counts (term frequencies)
        rows[ind:ind_end] = uniq_indices  # save the row index: index in
        doc_idx = np.where(docpaths == docpath)  # get the document index for the document name
        cols[ind:ind_end] = np.repeat(doc_idx, n_vals)  # save it as repeated value

        ind = ind_end  # resume with next document -> add data to the end

    # calculate the term df by counting the occurence of the unqiue indices per document -> result is sorted by index
    global_unique_indices, global_counts = np.unique(global_indices, return_counts=True)

    # calculation of idf
    idf = ndocs / global_counts

    # select idf according to indices in "rows" vector for DTM and multiply it with "data"(tf) vector -> tf-idf
    data = np.multiply(data, idf[rows])

    # Construct DTM as COO Matrix
    return coo_matrix((data, (rows, cols)), shape=(nvocab, ndocs), dtype=np.float32),  vocab[vocab_sorter], idf, docpaths

def convertDocToVec(vocab):
    print("convertDocToVec is not implemented yet!")
    return

def testTFIDF(docs = {
        'file1': ['ein', 'test', 'für', 'Dokument', 'eins'],
        'file21': ['ein', 'weiteres', 'Dokument'],
        'file22': ['ein', 'weiteres', 'Dokument'],
        'file3': ['alle', 'guten', 'Dinge', 'sind', 'drei'],
        'file4': ['ein', 'test', 'für', 'Dokument', 'drei'],
    }):

    print("Docs (order is random!):", docs)

    tfidf, vocab, idf, docPaths = createTFIDFMatrix(docs)

    print("TFIDF:",tfidf.toarray())
    print("Vocab:", vocab)
    print("IDF:", idf)
    print("DocPaths:", docPaths)

    return

#testTFIDF()


