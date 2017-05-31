# LatentSemanticIndexing by Team 3 (Hoffman, Portisch, Ulbrich, Hentschel) 
Repository for Task 3 of the Information Retrival team project: Latent Semantic Indexing.

## General Information

Used Technologies:
- Python and the Natural Language ToolKit (nltk) for Pyton
- Webpage as UI build with Angular

## Usage

To learn the model please execute following steps:

To use the model and execute queries please follow these steps:
1. Learn the model as described above
2. Execute the ``python /main.py``
3. Navigate to http:\\localhost:8000 in ur web browser

#### Highlevel-Taks
- speichern und retrieven von data-objekten (konkret: arrays und objekte) [Sascha] OUTPUT: Python Notebook (copy-paste Vorlage)
- read into Pooling Evaluation Method 
- familiarize with SVD & LSI


---------------------------------------------------------------------------------
#### Concrete Tasks

##### 1) Files einlesen [Alex, Jan]
- INPUT: Root Directory of Files
- OUTPUT: Directory

- one line: string sequence of 1 document (tokens -> you can decide which) 
- Format CSV (use semicolons for separation!) -> if possible save array


##### 2) Preprocessing [Alex, Jan]
- INPUT: directory aus 1
- OUTPUT: CSV ? aus 1 angepasst -> if possible save array

- Lemmatization / Stemming 
- Stopword Removal ?


##### 3) TF-IDF [Sascha]
- INPUT: CSV aus 2
- OUTPUT: TF-IDF Matrix (sparse Format) -> save (X)
-> (eine Spalte = Ein Dokument; Eine Zeile = ein Token) 


##### 4) SVD [Sascha]
- apply SVD
- set k
- save U, S (dense)


##### 5) "Search" [David]
- INPUT: U, S, Query
- OUTPUT: Document IDs

- Query-Transformation
- Cosine similarity


##### 6) Connect to Frontend [David]
- write service
