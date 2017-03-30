import numpy as np

### Temporary Mock data ####################################################

MOCK_DOCS = ['rec.sport.baseball/100521', 'rec.sport.baseball/101666', 'rec.sport.baseball/102151', 'sci.med/57110', 'sci.med/58047']
# ['data/20news-bydate/20news-bydate-train/rec.sport.baseball/100521']
MOCK_TERM_VECTOR = np.mat([1, 0, 0, 2]).T
MOCK_Sk = np.mat([[4,0],[0,1]])
MOCK_Uk = np.mat([[0.5, 0.4],[0.1, 0.2],[0.25,0.05],[0.15, 0.35]])
MOCK_VkTRANSPOSED = np.mat([[0.2,0.1,0.3,0.4,0.0],[0.1,0.3,0.2,0.1,0.3]])
MOCK_COS = np.mat([[0.15,0.35,0.28,0.19,0.33]])

############################################################################

def getTermVector(query = ''):
	## TODO function should be provided within the preprocessing process
	return MOCK_TERM_VECTOR

def unitifyVector(vector):
	return vector / vector.sum()

def mapVectorToLowerRank(d, sk = MOCK_Sk, uk = MOCK_Uk):
	skInverse = sk.I
	ukTransposed = uk.T
	return skInverse * ukTransposed * d

def computeCosineSimilarities(dk, vkTransposed = MOCK_VkTRANSPOSED):
	dkUnit = unitifyVector(dk)
	return dk.T * vkTransposed

def computeRankedList(cosineVector = MOCK_COS, docs = MOCK_DOCS):
	if cosineVector.shape[1] != len(docs):
		return []

	rankedDocs = []
	for i in range(0, cosineVector.shape[1]):
		rankedDocs.append((docs[i], cosineVector[0,i]))

	rankedDocs.sort(key=lambda tup: tup[1], reverse = True)
	return rankedDocs

def getRankedList(query, docs, uk, sk, vkTransposed):
	d = getTermVector(query)
	dk = mapVectorToLowerRank(d, sk, uk)
	cosVector = computeCosineSimilarities(dk, vkTransposed)
	return computeRankedList(cosVector, docs)

def getRankedListMock():
	d = getTermVector('')
	dk = mapVectorToLowerRank(d, MOCK_Sk, MOCK_Uk)
	cosVector = computeCosineSimilarities(dk, MOCK_VkTRANSPOSED)
	return computeRankedList(cosVector, MOCK_DOCS)

