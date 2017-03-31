import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import svds
from scipy.linalg import inv, norm

import tfidf


class SVDHandler:

    # Input: Term-Document-Matrix (Sparse COO), vector of DocPaths [, k]
    # returns U, S, V
    def __init__(self, tdm, docs, k = 50):
        if isinstance(tdm, coo_matrix):
            self.docs = docs

            #calc SVD
            self.U, s, self.V = svds(tdm, k = k)
            # TODO: own k determination and reduction accordingly

            #Further precalculations:
            self.S = np.diag(s)
            self.SiUt = inv(self.S).dot(self.U.transpose())
            self.Vt = self.V.transpose()
            tempNorms = np.diag(self.Vt).dot(self.V)
            tempNorms[tempNorms < 0] = 0
            self.docNorms = np.sqrt(tempNorms)

            return
        else:
            print("SVD: Error: Please provide Matrix in sparse COO format!")
            return

    #input
    def getRanking(self,vec):
        #convert to dense vector
        dv = self.SiUt.dot(vec)

        #Calculate similarity
        sim = (self.Vt.dot(dv))/(self.docNorms * norm(dv))

        #sort result
        sorter = np.argsort(sim)[::-1] #descending order

        #return sorted results
        return self.docs[sorter], sim[sorter]

def testSVD(docs = {
        'file1': ['ein', 'test', 'für', 'Dokument', 'eins'],
        'file21': ['ein', 'weiteres', 'Dokument'],
        'file22': ['ein', 'weiteres', 'Dokument'],
        'file3': ['alle', 'guten', 'Dinge', 'sind', 'drei'],
        'file4': ['ein', 'test', 'für', 'Dokument', 'drei'],
    }):
    tdm, vocab, idf, docPaths = tfidf.createTFIDFMatrix(docs)
    #tfidf.convertDocToVec()   pick first instead:
    vec = tdm.toarray()[:, 0]
    print("Input Doc:",docPaths[0],"Vec:",vec )

    svdHandler = SVDHandler(tdm, docPaths, k = 3)
    docs, sims = svdHandler.getRanking(vec)

    print("Ranked Docs:", docs )
    print("Similarities:", sims)

    return

#testSVD()