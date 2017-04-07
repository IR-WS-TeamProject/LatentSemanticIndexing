from lsi.lsiHandler import LSIHandler


class LSIEvaluator:

    def train(self,
              max_k=100,
              bag_of_words="bow_porter.dict"):
        #Init Handler with training set
        self.lsi_handler = LSIHandler(
                                load_tfidf=False,
                                load_svd=False,
                                max_k=max_k,
                                bag_of_words = bag_of_words
                                )

    def evaluate(self,
                 bag_of_words="..."):




