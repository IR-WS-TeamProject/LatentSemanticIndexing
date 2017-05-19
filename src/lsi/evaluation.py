from lsi.lsiHandler import LSIHandler
import numpy as np


class LSIEvaluator:

    def train(self,
              bag_of_words,
              max_k,
              load_tdm=True,
              load_svd=False):
        #Init Handler with training set
        print("Evaluation: Initialize LSI with train data ", bag_of_words)
        self.lsi_handler = LSIHandler(
                                load_tdm=load_tdm,
                                load_svd=load_svd,
                                max_k=max_k,
                                bag_of_words = bag_of_words
                                )


    def evaluate(self,
                 bag_of_words,
                 n=10,
                 load_tdm=False):
        print("Evaluation: Start evaluation based on test data ", bag_of_words)
        #### 1) Eval. LSI
        lsi_ranking = self.lsi_handler.getRankingBatch(bag_of_words,
                                                        n=n,
                                                        load_tdm=load_tdm,
                                                       use_SVD=True)

        print("Evaluation: LSI Rankings calculated, KPIs:")
        self.calculate_NewsGroupRatio(lsi_ranking)

        #### 2) Eval. VSM
        vsm_ranking = self.lsi_handler.getRankingBatch(bag_of_words,
                                                       n=n,
                                                       load_tdm=load_tdm,
                                                       use_SVD=False)

        print("Evaluation: VSM Rankings calculated, KPIs:")
        self.calculate_NewsGroupRatio(vsm_ranking)


    def calculate_NewsGroupRatio(self,ranking):
        #KPI: Average same news group ratio
        same_ng_ratio = np.empty(len(ranking.keys()), dtype=np.float32)
        ind = 0
        for test_doc, result in ranking.items():
            test_ng = test_doc.split("/")[0]
            result_docs = result["docs"]
            total = len(result_docs)
            equal_ng = [1 for doc in result_docs if doc.split("/")[0] == test_ng]
            same_ng_ratio[ind] = sum(equal_ng)/total
            ind += 1

        print("Evaluation: KPI - Average ratio of result docs being in same news group as test doc: ",
              np.average(same_ng_ratio))

    #TODO: Further KPIs?







