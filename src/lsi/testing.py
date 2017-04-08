from lsi.lsiHandler import LSIHandler
from lsi.evaluation import LSIEvaluator

############################## TESTING ################################################
def testLSI(load_tfidf=True,
            load_svd=True,
            max_k=150):
    #import timeit

    # In server: create instance just once on startup
    lsi_handler = LSIHandler(load_tfidf=load_tfidf,
                             load_svd=load_svd,
                             max_k=max_k)

    # In server: per query
    documents, similarities = lsi_handler.getRanking(
        query="source of orbital element sets other than UAF/Space Command",  # Doc sci.space/60158
    )

    print("Result - Top-10 Docs:", documents)
    print("Result - Similarities:", similarities)
    #print("Result - Ranking 2:", lsi_handler.getRanking2()) -> Error

    #Perf. Measurement:
    #print("Result - Runtimes: Init: ", timeit.timeit(LSIHandler,number=1))
    #print("Result - Runtimes: Rank: ", timeit.timeit(lsi_handler.getRanking,number=1))

#testLSI()

def testEvaluator():
    evaluator = LSIEvaluator()
    evaluator.train(bag_of_words="bow_porter.dict",
                    max_k=150,
                    load_svd=True) # False: forces recalculation of SVD
    evaluator.evaluate(bag_of_words="bow_porter_testData.dict",
                       load_tdm=True) # reuse TDM, if new bag of words stays same: set to False!

testEvaluator()