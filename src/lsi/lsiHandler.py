import lsi.tfidf as tfidf
import lsi.svd as svd
from preprocessing.PorterFilePreprocessing import PorterFilePreprocessing as fp
import os

import lsi.queryexec as qe
import numpy as np

class LSIHandler:
    def __init__(self,
                 files_path=os.pardir + "/files/",
                 load_tfidf=True, #set to False if TF-IDF Matrix should be recalculated rather than loaded from disk
                 load_svd=True, #set to False if SVD should be recalculated rather than loaded from disk
                 max_k=100,
                 bag_of_words = "bow_porter.dict"):
        """Initialize all handlers (once and not per query)"""

        #TF-IDF
        self.tfidf_handler = tfidf.TFIDFHandler(docs=files_path + bag_of_words,
                                                path=files_path,
                                                load=load_tfidf)
        #SVD
        self.svd_handler = svd.SVDHandler(tdm=self.tfidf_handler.getTDM(),
                                          docs=self.tfidf_handler.getDocuments(),
                                          max_k=max_k,
                                          path=files_path,
                                          load=load_svd)
    def getRanking(self,
                   query="",
                   n=10):
        """Retrieve top-n ranking based on query string."""
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
        return self.svd_handler.getRanking(vec=term_vec, n=n)

    def getRanking2(self,
                    query = "",
                    ):
        return qe.get_ranked_list(query=query,
                           docs=self.tfidf_handler.getDocuments(),
                           u_k=np.mat(self.svd_handler.Ut.transpose()),
                           s_k=np.mat(np.diag(self.svd_handler.s)),
                           v_k_transposed=np.mat(self.svd_handler.V.transpose()))


