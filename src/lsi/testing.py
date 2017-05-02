from lsi.lsi_handler import LSIHandler
from lsi.evaluation import LSIEvaluator
import os, sys

#add src package as additional source of modules
module_path = os.path.abspath(os.path.join('../'))
if module_path not in sys.path:
    sys.path.append(module_path)

############################## TESTING ################################################
def testLSI(load_tdm=True,
            load_svd=True,
            max_k=150):
    #import timeit

    # In server: create instance just once on startup
    lsi_handler = LSIHandler(load_tdm=load_tdm,
                             load_svd=load_svd,
                             max_k=max_k)

    # In server: per query
    documents, similarities = lsi_handler.get_ranking(
        query="source of orbital element sets other than UAF/Space Command",   # Doc sci.space/60158
        use_SVD=False
    )

    print("Result - Top-10 Docs:", documents)
    print("Result - Similarities:", similarities)
    #print("Result - Ranking 2:", lsi_handler.getRanking2()) -> Error

    #Perf. Measurement:
    #print("Result - Runtimes: Init: ", timeit.timeit(LSIHandler,number=1))
    #print("Result - Runtimes: Rank: ", timeit.timeit(lsi_handler.getRanking,number=1))


def testEvaluator(
        max_k=150,
        load_tdm=True,
        load_svd=False
):
    evaluator = LSIEvaluator()
    evaluator.train(bag_of_words="bow_lemmatization_train_data.dict",
                    max_k=max_k,
                    load_tdm=load_tdm, # False: forces recalculation of TFIDF TDM (case: new train bow)
                    load_svd=load_svd) # False: forces recalculation of SVD (case: new bow or change of k)
    evaluator.evaluate(bag_of_words="bow_lemmatization_test_data.dict",
                       load_tdm=load_tdm) # False: forces recalculation of TFIDF TDM for test data
                                            # (case: new test or train bow)

#TEST LSI
testLSI()

#run onces if new bow:
#testEvaluator(max_k=50,load_tdm=False) # forcing tdm re-calculation

#run batch testing
#for k in [100,150,200,250]:
#    print("#### TEST RUN: k = ",k," ####")
#    testEvaluator(max_k=k)