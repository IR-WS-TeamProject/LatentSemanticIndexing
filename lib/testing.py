import tfidf
import svd
import json


tfidfHandler = tfidf.TFIDFHandler(docs = "files/bow.dict", loadPath = "files/")


print("Start SVD")
svdHandler = svd.SVDHandler(tfidfHandler.getTDM(), tfidfHandler.getDocs(), maxK = 1)
print("Finished SVD")

query = ['Clark', 'deserve', 'first', 'star', 'Gilmour'] #Doc 52555
print("Tested Query:", query)
vec = tfidfHandler.convertDocToVec(query)
print("As Vec:", vec)

docs, sims = svdHandler.getRanking(vec)

print("Ranked Docs:", docs )
print("Similarities:", sims)

