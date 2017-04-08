import numpy as np
from scipy.sparse import coo_matrix, csc_matrix, csr_matrix
from scipy.sparse.linalg import svds
from scipy.linalg import inv, norm
from scipy import matrix
import sys
import lsi.tfidf


class SVDHandler:

    # Input: Term-Document-Matrix (Sparse COO), vector of DocPaths , maximum k, path to save to/load from file, indicator if load should be used (false = re-calculation)
    def __init__(self, tdm,
                 max_k=100,
                 path=None,
                 load=True):

        self.isValid = True
        if(load):
            if(path is not None):
                try:
                    self.__load__(path)
                    print("SVD: Loaded from files")
                except:
                    print("SVD: Load from files failed - ", sys.exc_info()[0], " (",sys.exc_info()[1],")")
                    load = False
            else:
                print("SVD: Load from files failed - please specify path")
                load = False

        if(not load):
            print("SVD: Start calculation")
            if isinstance(tdm, coo_matrix):
                #self.docs = docs
                #calc SVD
                U, s, Vt = svds(tdm, k = max_k)
                # TODO: own k determination? -> set s = 0 for truncation (or just rely on k-tuning?)
                #test (truncate lowest eigenvalue):
                #s[:-22] = 0

                #truncate SVD (s is ordered ascending! -> find min index where s is non-zero)
                s_min = np.min(s.nonzero())
                self.s = s[s_min:]#-1]
                self.k = len(self.s)
                U = U[:,s_min:]#-1]
                Vt = Vt[s_min:,:]#-1,:]

                #Further precalculations:
                self.Ut = U.transpose()
                self.SiUt = inv(np.diag(self.s)).dot(self.Ut) #numpy.dot: For 2-D arrays it is the matrix product
                self.V = Vt.transpose()
                #tempNorms = np.diag(self.Vt).dot(self.V)
                #tempNorms[tempNorms < 0] = 0
                #self.docNorms = np.sqrt(tempNorms)
                self.docNorms = np.sum(self.V**2,axis=-1)**(1./2)

                if(path is not None):
                    self.__save__(path)
            else:
                print("SVD: Error: Please provide Matrix in sparse COO format and docs")
                self.isValid = False
        return

    def __save__(self,path):
        np.save(path + "svd.k", self.k)
        np.save(path + "svd.s", self.s)
        np.save(path + "svd.Ut", self.Ut)
        #np.save(path + "svd.SiUt", self.SiUt)
        np.save(path + "svd.V", self.V)
        np.save(path + "svd.docNorms", self.docNorms)
        #np.save(path + "svd.docs", self.docs)
        print("SVD: Saved to files")
        return

    def __load__(self,path):
        self.k = np.load(path + "svd.k.npy")
        self.s = np.load(path + "svd.s.npy")
        self.Ut = np.load(path + "svd.Ut.npy")
        # self.SiUt       = np.load(path + "svd.SiUt.npy")
        self.V = np.load(path + "svd.V.npy")
        self.docNorms = np.load(path + "svd.docNorms.npy")
        # self.docs = np.load(path + "svd.docs.npy")

        self.SiUt = inv(np.diag(self.s)).dot(self.Ut)
        return

    #input: dense topic vector, # of top ranked docs
    #output: ranking
    def getRanking(self,vec,n = 10):
        #convert to dense vector
        dv = self.SiUt.dot(vec)

        #Calculate similarity
        sim = (self.V.dot(dv))/(self.docNorms * norm(dv))

        #Top-n result indices
        topn = np.argsort(sim)[::-1][:n] #descending order, taking top N

        #return sorted results
        return topn, sim[topn]

    def getRankingBatch(self, matrix):
        # convert to dense vectors (matrix)
        # - bit complicated because of elementwise dot product between dense and sparse matrix needed!
        # - COO Matrix no appropriate - but CSC and SCR is supporting vector products.
        # -- Column compressed for input matrix because each column (doc) vector is neede
        # -- Row compressed for SiUt because each row (topics) is needed
        #dm = self.SiUt.dot(matrix.tocsc()) -> dot product method of sparse matrix needed -> convert
        topic_m = csr_matrix(self.SiUt).dot(matrix.tocsc()).todense()

        print("Ranking: Batch - calculated dense topic matrix (shape: ",topic_m.shape,")")

        # Calculate similarity for each train docs - test docs combination
        # first: train doc norms (x) test doc norms has same same structure as V*topic_m (doc wise dot product)
        norms = np.outer(self.docNorms, np.linalg.norm(topic_m,axis=0))
        sim = np.array(self.V.dot(topic_m) / norms) #element-wise devision

        print("Ranking: Batch - calculated similarities")

        # return result matrix
        return sim





def testSVD(docs = {
        'file1': ['ein', 'test', 'für', 'Dokument', 'eins'],
        'file21': ['ein', 'weiteres', 'Dokument'],
        'file22': ['ein', 'weiteres', 'Dokument'],
        'file3': ['alle', 'guten', 'Dinge', 'sind', 'drei'],
        'file4': ['ein', 'test', 'für', 'Dokument', 'drei'],
    }):
    tfidfHandler = lsi.tfidf.TFIDFHandler(docs= docs, load = False)
    #tfidf.convertDocToVec()   pick first instead:
    query = ['ein', 'ein', 'weiteres', 'Dokument']
    print("Query:", query)
    vec = tfidfHandler.convertBoWToTermVector(query)
    print("Vec:", vec)

    svdHandler = SVDHandler(tfidfHandler.getTDM(), max_k= 3)
    docs, sims = svdHandler.getRanking(vec)
#matrix.
    print("Ranked Docs:", docs )
    print("Similarities:", sims)

    return

#testSVD()