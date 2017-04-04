import lsi.tfidf as tfidf
import lsi.svd as svd
import os
#import PorterFilePreprocessing as fp

# ---------- Init (once and not per query)

#TF-IDF
filesPath =  os.pardir + "/files/"
tfidfHandler = tfidf.TFIDFHandler(docs=filesPath+"bow.dict", path=filesPath , load = True)
#SVD
svdHandler = svd.SVDHandler(tdm=tfidfHandler.getTDM(), docs=tfidfHandler.getDocs(), max_k = 30, path=filesPath, load = False)

# -------- Handle Single Query
query = "MIT Lincoln LaboratoryDistribution: source of orbital element sets other than UAF/Space Command. I believe there is one on CompuServe." # Doc sci.space/60158

#Convert into term vector
#bow = fp.stringTransformation(query)
bow  = ['underground','underwater','wireless','communications'] #Doc sci.electronics/52434
print("Test TermVec:", bow)

#convert into topic vector (SVD)
termVec = tfidfHandler.convertBoWToTermVector(bow)
print("TopicVec, Non-Zero pos:", termVec.nonzero())
print("TopicVec, Non-Zero values:", termVec[termVec.nonzero()])
print("TopicVec, size:", termVec.size)

#Calc. LSI ranking
docs, sims = svdHandler.getRanking(termVec, n = 10)
print("Top-10 Docs:", docs )
print("Similarities:", sims)

