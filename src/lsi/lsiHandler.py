import lsi.tfidf as tfidf
import lsi.svd as svd
#import PorterFilePreprocessing as fp
import os

import lsi.queryexec as qe
import numpy as np

class LSIHandler:
    def __init__(self,
                 files_path=os.pardir + "/files/",
                 load_tfidf=True, #set to False if TF-IDF Matrix should be recalculated rather than loaded from disk
                 load_svd=True, #set to False if SVD should be recalculated rather than loaded from disk
                 max_k=100):
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
        bow = stringTransformation(query)
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
                    query = "source of orbital element sets other than UAF/Space Command",  # Doc sci.space/60158
                    ):
        return qe.get_ranked_list(query=query,
                           docs=self.tfidf_handler.getDocuments(),
                           u_k=np.mat(self.svd_handler.Ut.transpose()),
                           s_k=np.mat(np.diag(self.svd_handler.s)),
                           v_k_transposed=np.mat(self.svd_handler.V.transpose()))

############################## TEMPORARY CODING ########################################

from nltk.stem.porter import *
from nltk.corpus import stopwords
import nltk

def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


# this method returns a string array with the words of the document
# it needs to be used for query preprocessing as well
def stringTransformation(inputString):
    #corpora -> stopwords
    #nltk.download()

    # does it really work like this? Do I have to cast the input Parameter?! I hate this ducktyping...
    returnString = str(inputString)

    # lower case transformation
    returnString = returnString.lower()


    returnString = ''.join(i for i in returnString if ord(i) < 128) # this limits the allowed characters to ASCI II

    adict = {
        "from:": "",
        "subject:": "",
        "re:": "",
        "organization:": "",
        "distribution:": "",
        "lines:": "",
        "reply-to:": "",

        ": ": " ",              # allows for tokens like "12:00:30"
        ". ": " ",              # allows for tokens like "10.50" or dates like "2017.03.05"
        ", ": " ",              # allows for tokens like 5,5 (German decimal)

        "\n": " ",              # handle line breaks
        ".\n": " ",
        ".\"" : " ",
        ".\'" : " ",
        "..": " ",
        ",\n": " ",
        ":\n": " ",

        "!": "",                # ascii 33
        '\"': "",               # ascii 34: quotation marks
        "#": "",                # ascii 35
        "$": "",                # ascii 36
        "%": "",                # ascii 37
        "&": "",                # ascii 38
        "\'": "",               # ascii 39: single quote
        "(": "",                # ascii 40
        ")": "",                # ascii 41
        "*": "",                # ascii 42
        "+": "",                # ascii 43
        "-": "",                # ascii 45
        "/": "",                # ascii 47

        ";": "",                # ascii 59
        "<": "",                # ascii 60
        "=": "",                # ascii 61
        ">": "",                # ascii 62
        "?": "",                # ascii 63

        "[": "",                # ascii 91
        "\\": "",               # ascii 92
        "]": "",                # ascii 93
        "^": "",                # ascii 94
        "_": "",                # ascii 95
        "`": "",                # ascii 96

        "{": "",                # ascii 123
        "|": "",                # ascii 124
        "}": "",                # ascii 125
        "~": ""                 # ascii 126
    }

    # delete/replace special characters
    returnString = multiple_replace(returnString, adict)

    # create tokens
    returnString = returnString.split(" ")

    #remove empty entries
    returnString = [x for x in returnString if x]

    #stopword list
    stopWordList = set(stopwords.words('english'))

    # porter stemmer
    stemmer = PorterStemmer()

    # Stopword Removal and Stemming
    # Remarks: the current nltk porter stemmer has some known issues with "oed"
    newReturnString = []
    for currentToken in returnString:
        if (currentToken not in stopWordList) and currentToken != "oed": #porter stemmer cannot handle that

            # handling cases when the last character is a '.' (this should not be the case but causes an exception with the stemmer)
            if currentToken.endswith("."):
                currentToken = currentToken[:len(currentToken) - 1]

            # print(currentToken)
            stemmer.stem(currentToken)
            newReturnString.append(currentToken)

        elif currentToken == "oed": # add oed without stemming
            newReturnString.append("oed")

    returnString = newReturnString

    return returnString



############################## TESTING ################################################
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

#testLSI()