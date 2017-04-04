import numpy as np
from scipy.sparse import coo_matrix, save_npz , load_npz
import json
import sys

class TFIDFHandler:
    #Input: Dict or filepath to json encoded dict, or a path to load from/save to, a flag to indicate if stored files should be loaded (false = re-calculation)
    #returns TFIDF COO-Matrix and sorted Vocabulary + IDF-Vector
    def __init__(self, docs = None, path = None, load = True):
        #Handle input formats (target: dict)
        if(load and path is not None): #try to load
            try:
                self.tdm = load_npz(path + "tfidf.tdm.npz")

                self.docpaths = np.load(path + "tfidf.docs.npy")
                self.vocab = np.load(path + "tfidf.vocab.npy")
                self.idf= np.load(path + "tfidf.idf.npy")

                print("TF-IDF: Loaded from files")
            except:
                print("TF-IDF: Load from files failed - ", sys.exc_info()[0], " (",sys.exc_info()[1],")")

                load = False

        if(not load and docs is not None): #Docs provided and data not loaded -> load docs and calculate TF-IDF
            if not isinstance(docs,dict):
                if isinstance(docs, str):
                    print("TF-IDF: Load docs from file")
                    try:
                        with open(docs, 'r') as infile:
                            docs = json.load(infile)
                    except:
                        print("TF-IDF: Error: Load of docs failed - ", sys.exc_info()[0], " (", sys.exc_info()[1], ")")
                        return
                else:
                    print("TF-IDF: Error: Load of docs failed - Unsupported format of documents as input!")
                    return
            self.__createTFIDF__(docs)
            if(path is not None):
                self.__save__(path)
        elif(not load and docs is None):
            print("TF-IDF: Error: No load of existing TF-IDF and no Docs specified")
        return



    def __createTFIDF__(self, docs):
        # Based on: https://datascience.blog.wzb.eu/2016/06/17/creating-a-sparse-document-term-matrix-for-topic-modeling-via-lda/
        # -> adapted to fit TermxDoc Matrix without additional transpose at the end

        print("TF-IDF: Start creation")

        # Init Vocabulary (Set)
        vocab = set()
        # Init Count of Non-Zero Values
        n_nonzero = 0

        # Iterate over documents to create vocabulary
        for docterms in docs.values():
            unique_terms = set(docterms)  # all unique terms of this doc (set of terms)
            vocab |= unique_terms  # set union: add unique terms of this doc
            n_nonzero += len(unique_terms)  # increase Non-Zero count by adding count of unique terms in this doc

        # convert to numpy for processing
        self.docpaths = np.array(list(
            docs.keys()))  # keys of dictionary (order of dictionary is used, but this doesn't correspond to order of inserts!)
        self.vocab = np.array(list(vocab))

        # Array containing sorted indices
        vocab_sorter = np.argsort(self.vocab)

        # print(vocab_sorter) #sorted indizes
        # print(vocab[vocab_sorter]) #outputs sorted vocabulary

        ndocs = len(self.docpaths)
        nvocab = len(self.vocab)

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
            term_indices = vocab_sorter[np.searchsorted(self.vocab, terms, sorter=vocab_sorter)]

            # count the unique terms of the document and get their vocabulary indices
            uniq_indices, counts = np.unique(term_indices, return_counts=True)

            #adapt tf to consider doc length and dampen effect of large counts
            #tf(t, d) = (1 + log10(ft, d)) / (1 + log10(max{ft’, d: t’ ∈ d}))
            tf = (1 + np.log10(counts) / (1 + np.log10(np.max(counts))))

            # add (unique) indices of current doc to a list which is later on used for df
            global_indices.extend(uniq_indices)

            n_vals = len(uniq_indices)  # = number of unique terms
            ind_end = ind + n_vals  # to  is the slice that we will fill with data

            data[ind:ind_end] = tf  # save the counts (term frequencies)
            rows[ind:ind_end] = uniq_indices  # save the row index: index in
            doc_idx = np.where(self.docpaths == docpath)  # get the document index for the document name
            cols[ind:ind_end] = np.repeat(doc_idx, n_vals)  # save it as repeated value

            ind = ind_end  # resume with next document -> add data to the end

        # calculate the term df by counting the occurence of the unqiue indices per document -> result is sorted by index
        global_unique_indices, global_counts = np.unique(global_indices, return_counts=True)

        # calculation of idf
        self.idf = np.log10(ndocs / np.array(global_counts))

        # select idf according to indices in "rows" vector for DTM and multiply it with "data"(tf) vector -> tf-idf
        data = np.multiply(data, self.idf[rows])

        # Construct DTM as COO Matrix
        self.tdm = coo_matrix((data, (rows, cols)), shape=(nvocab, ndocs), dtype=np.float32)
        #self.vocab = vocab[vocab_sorter]

        print("TF-IDF: Finished creation")

        return

    def getTDM(self):
        return self.tdm

    def getVocab(self):
        return self.vocab

    def getDocs(self):
        return self.docpaths

    def convertDocToVec(self,doc):
        #identifiy which indicies of term-vector match
        indices = [np.where(self.vocab == item) for i, item in enumerate(doc) if item in self.vocab]
        #count how often which index occures and calculate tf
        indices_unique, counts = np.unique(indices, return_counts=True)
        tf = (1 + np.log10(counts) / (1 + np.log10(np.max(counts))))
        #init target vec with zeros
        vec = np.zeros(len(self.vocab), dtype=np.float32)
        #fill vec according to tf-idf
        vec[indices_unique] = tf * self.idf[indices_unique]
        return vec

    def __save__(self, path):
        save_npz(path + "tfidf.tdm",self.tdm) #sparse save

        np.save(path + "tfidf.docs",self.docpaths)
        np.save(path + "tfidf.vocab", self.vocab)
        np.save(path + "tfidf.idf", self.idf)

        print("TF-IDF: Saved")
        return


def testTFIDF(docs = {
        'file1': ['ein', 'test', 'für', 'Dokument', 'eins'],
        'file21': ['ein', 'weiteres', 'Dokument'],
        'file22': ['ein', 'weiteres', 'Dokument'],
        'file3': ['alle', 'guten', 'Dinge', 'sind', 'drei'],
        'file4': ['ein', 'test', 'für', 'Dokument', 'drei'],
    }):

    print("Docs (order is random!):", docs)

    tfidfHandler = TFIDFHandler(docs)

    print("TFIDF:",tfidfHandler.getTDM().toarray())
    print("Vocab:", tfidfHandler.getVocab())
    print("DocPaths:", tfidfHandler.getDocs())

    query = ['ein','ein','weiteres','Dokument']
    print("Query:", query)
    print("Vec:",tfidfHandler.convertDocToVec(query))

    return

#testTFIDF()

