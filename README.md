# LatentSemanticIndexing
Repository for Task 3: Latent Semantic Indexing.




Highlevel-Taks
- speichern und retrieven von data-objekten (konkret: arrays und objekte) [Sascha] OUTPUT: Python Notebook (copy-paste Vorlage)
- read into Pooling Evaluation Method 
- familiarize with SVD & LSI


---------------------------------------------------------------------------------
Concrete Tasks

1) Files einlesen [Alex, Jan]
INPUT: Root Directory of Files
OUTPUT:

- one line: string sequence of 1 document (tokens -> you can decide which) 
- Format CSV (use semicolons for separation!) -> if possible save array
- 


2) Preprocessing [Alex, Jan]
- Lemmatization / Stemming 
- Stopwords?

INPUT: CSV aus 1
OUTPUT: CSV aus 1 angepasst -> if possible save array


3) TF-IDF [Sascha]
INPUT: CSV aus 2
OUTPUT: TF-IDF Matrix (sparse Format) -> save (X)
(eine Spalte = Ein Dokument; Eine Zeile = ein Token) 


4) SVD [Sascha]
- apply SVD
- set k
- save U, S (dense)


5) "Search" [David]
INPUT: U, S , Query
OUTPUT: Document IDs
- Query-Transformation
- Cosine similarity


6) Connect to Frontend [David]
- 
