import tfidf
import svd

# ---------- Init (once and not per query)
#TF-IDF
tfidfHandler = tfidf.TFIDFHandler(docs = "files/bow.dict", path="files/", load = True)
#SVD
svdHandler = svd.SVDHandler(tdm=tfidfHandler.getTDM(), docs=tfidfHandler.getDocs(), maxK = 200, path="files/", load = True)

# -------- Handle Single Query
query = "MIT Lincoln LaboratoryDistribution: source of orbital element sets other than UAF/Space Command. I believe there is one on CompuServe." # Doc sci.space/60158

#Convert into term vector
#TODO: Process raw query -> termVector
termVec  = ['underground','underwater','wireless','communications'] #Doc sci.electronics/52434
print("Test TermVec:", termVec)

#convert into topic vector (SVD)
topicVec = tfidfHandler.convertDocToVec(termVec)
print("As Vec, Non-Zero pos:", topicVec.nonzero())
print("As Vec, Non-Zero values:", topicVec[topicVec.nonzero()])
print("As Vec, size:", topicVec.size)

#Calc. LSI ranking
docs, sims = svdHandler.getRanking(topicVec, n = 10)
print("Top-10 Docs:", docs )
print("Similarities:", sims)

