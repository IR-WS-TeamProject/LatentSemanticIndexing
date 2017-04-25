import lsi.tfidf as tfidf
import lsi.svd as svd
from preprocessing.PorterFilePreprocessing import PorterFilePreprocessing as fp
import os
import sys
from scipy.sparse import save_npz , load_npz
from scipy.sparse.linalg import norm

import lsi.queryexec as qe
import numpy as np

#add src package as additional source of modules
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

class LSIHandler:
    def __init__(self,
                 bag_of_words="bow_lemmatization_train_data.dict",
                 files_path=os.pardir + "/files/",
                 load_tdm=True, #set to False if TF-IDF Matrix should be recalculated rather than loaded from disk
                 load_svd=True, #set to False if SVD should be recalculated rather than loaded from disk
                 max_k=100):
        """Initialize all handlers (once and not per query)"""
        self.isValid = False
        #TF-IDF
        self.tfidf_handler = tfidf.TFIDFHandler(docs=files_path + bag_of_words,
                                                path=files_path,
                                                load=load_tdm)

        if(self.tfidf_handler.isValid):
            #SVD
            self.svd_handler = svd.SVDHandler(tdm=self.tfidf_handler.getTDM(),
                                              max_k=max_k,
                                              path=files_path,
                                              load=load_svd)

            if(self.svd_handler.isValid):
                self.isValid = True
    def getRanking(self,
                   query="",
                   n=10):
        """Retrieve top-n ranking based on query string."""
        if(self.isValid):
            print("Ranking - Query: ", query)

            #Preprocess string: Convert into bag of words
            bow = fp.stringTransformation(query)
            #bow  = ['underground','underwater','wireless','communications'] #Doc sci.electronics/52434
            print("Ranking - BoW: ", bow)

            #Convert into term vector (SVD)
            term_vec = self.tfidf_handler.convertBoWToTermVector(bow)
            print("Ranking - Term Vector: Non-Zero positions:", term_vec.nonzero())
            print("Ranking - Term Vector: Non-Zero values:", term_vec[term_vec.nonzero()])
            print("Ranking - Term Vector: Size:", term_vec.size)

            #Calc. LSI ranking
            doc_ind, similarities = self.svd_handler.getRanking(vec=term_vec, n=n)
            return self.tfidf_handler.getDocuments(doc_ind), similarities
        else:
            print("Ranking: Error - Instantiation of LSI failed")
            return [""], [0]

    def getRankingBatch(self,
                 bow=None,
                 files_path=os.pardir + "/files/",
                 load_tdm=False, #if true: try to load tfidf from file
                 n=None,  #if speciefied, just topn dic is returned else: full similarity matrix
                 use_SVD=True #if false: VSM based similarity used
                 ):
        # 1) Convert input bag of words into term document matrix (sparse!) [or load from file]
        if(load_tdm):
            try:
                new_docs_tdm = load_npz(files_path + "lsi.ranking.tdm.npz")
                new_docs_paths = np.load(files_path + "lsi.ranking.docpaths.npy")
                print("Ranking: Loaded cached term-doc-matrix")
            except:
                load_tdm = False
                print("Ranking: Load of cached term-doc-matrix failed!")

        if(not load_tdm and bow is not None):
            new_docs_tdm, new_docs_paths = self.tfidf_handler.convertBoWToTermVectorBatch(files_path + bow)
            save_npz(files_path + "lsi.ranking.tdm", new_docs_tdm)
            np.save(files_path + "lsi.ranking.docpaths", new_docs_paths)
            print("Ranking: Term-doc-matrix created and saved for new docs")
        elif(not load_tdm and bow is None):
            print("Ranking: Error - Please provide bag of word or save term-doc-matrix")
            return

        # 2) Get Similarities for each new doc - train doc combination
        if(use_SVD):
            similarities = self.svd_handler.getRankingBatch(new_docs_tdm)
        else:
            train_tdm = self.tfidf_handler.getTDM()
            new_docs_tdm = new_docs_tdm.tocsc()
            # rows of transposed train TDM  = docs -> element-wise dot with cols of new_docs_tdm (docs as well)
            train_dtm = train_tdm.transpose().tocsr()
            norms = np.outer(norm(train_dtm, axis=1),norm(new_docs_tdm, axis=0)) # Normalize
            similarities = np.array(train_dtm.dot(new_docs_tdm) / norms)
            print("Ranking: Batch - calculated VSM similarities. Shape ",similarities.shape)

        #Save for further analysis?
        #np.save(files_path + "eval.similarities", similarities)
        #print("Evaluation: Saved doc similarities in ", files_path)

        if (n is None): #no topn -> return raw similarity matrix
            return similarities
        else:
            new_doc_topn = {}
            for j, new_doc_sim in enumerate(similarities.transpose()):
                topn = np.argsort(new_doc_sim)[::-1][:n]
                result_docs = self.tfidf_handler.getDocuments(topn)
                result_similarities = new_doc_sim[topn]
                new_doc_topn[new_docs_paths[j]] = {"docs": result_docs,
                                                   "similarities": result_similarities}

            return new_doc_topn


    def getRanking2(self,
                    query = "",
                    ):
        return qe.get_ranked_list(query=query,
                           docs=self.tfidf_handler.getDocuments(),
                           u_k=np.mat(self.svd_handler.Ut.transpose()),
                           s_k=np.mat(np.diag(self.svd_handler.s)),
                           v_k_transposed=np.mat(self.svd_handler.V.transpose()))


