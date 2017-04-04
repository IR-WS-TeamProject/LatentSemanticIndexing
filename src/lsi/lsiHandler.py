import lsi.tfidf as tfidf
import lsi.svd as svd
#import PorterFilePreprocessing as fp
import os

import lsi.queryexec as qe
import numpy as np

class LSIHandler:
    def __init__(self,
                 files_path=os.pardir + "/files/",
                 load_tfidf=True,
                 load_svd=True,
                 max_k=30):
        """Initialize all handlers (once and not per query)"""

        #TF-IDF
        self.tfidf_handler = tfidf.TFIDFHandler(docs=files_path + "bow.dict",
                                                path=files_path,
                                                load=load_tfidf)
        #SVD
        self.svd_handler = svd.SVDHandler(tdm=self.tfidf_handler.getTDM(),
                                          docs=self.tfidf_handler.getDocuments(),
                                          max_k=max_k,
                                          path=files_path,
                                          load=load_svd)
    def getRanking(self,
                   query="source of orbital element sets other than UAF/Space Command",# Doc sci.space/60158
                   n=10):
        """Retrieve top-n ranking based on query string."""
        print("Ranking - Query: ", query)

        #Preprocess string: Convert into bag of words
        #bow = fp.stringTransformation(query)
        bow  = ['underground','underwater','wireless','communications'] #Doc sci.electronics/52434
        print("Ranking - BoW: ", bow)

        #Convert into term vector (SVD)
        term_vec = self.tfidf_handler.convertBoWToTermVector(bow)
        print("Ranking - Term Vector: Non-Zero positions:", term_vec.nonzero())
        print("Ranking - Term Vector: Non-Zero values:", term_vec[term_vec.nonzero()])
        print("Ranking - Term Vector: Size:", term_vec.size)

        #Calc. LSI ranking
        return self.svd_handler.getRanking(vec=term_vec, n=n)

    def getRanking2(self,
                    query = "source of orbital element sets other than UAF/Space Command",  # Doc sci.space/60158
                    ):
        return qe.get_ranked_list(query=query,
                           docs=self.tfidf_handler.getDocuments(),
                           u_k=np.mat(self.svd_handler.Ut.transpose()),
                           s_k=np.mat(np.diag(self.svd_handler.s)),
                           v_k_transposed=np.mat(self.svd_handler.V.transpose()))

def testLSI():
    #import timeit

    # In server: create instance just once on startup
    lsi_handler = LSIHandler()

    # In server: per query
    documents, similarities = lsi_handler.getRanking()

    print("Result - Top-10 Docs:", documents)
    print("Result - Similarities:", similarities)
    #print("Result - Ranking 2:", lsi_handler.getRanking2()) -> Error

    #Perf. Measurement:
    #print("Result - Runtimes: Init: ", timeit.timeit(LSIHandler,number=1))
    #print("Result - Runtimes: Rank: ", timeit.timeit(lsi_handler.getRanking,number=1))

testLSI()