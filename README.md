# LatentSemanticIndexing by Team 3 (Hofmann, Portisch, Ulbrich, Hentschel) 
Repository for Task 3 of the Information Retrival team project: Latent Semantic Indexing.

## General Information

Used Technologies:
- Python
- Libraries
    - Natural Language ToolKit (NLTK) for Python
    - Numpy
    - SciPy (v0.19)
    - json
- Webpage as UI build with Angular
- We recommend using Anaconda as package manager and runtime (https://www.continuum.io/downloads)

## How to Run
Preprocessed files are persisted and already available in the project.
If you want to re-preprocess, follow the steps of "How to Run from Scratch".

1. Copy the ``20news-bydate`` folder into ``LatentSemanticIndexing/data`` 
2. Execute ``python /main.py``
3. Navigate to [http://localhost:8000](http://localhost:8000 "Localhost - Port 8000") in your web browser.
4. If successful, the user interface of the search should appear.


## How to Run from Scratch
It is assumed that the newsgroup folder is available as described above.

1. Go to ``src/preprocessing/LemmatizationFilePreprocessing``
2. If you have never used the NLTK stopword removal list and the tokenizer, follow the subsequet steps. Otherwise continue with step 3.

 Execute 
 
    import nltk
    nltk.download()

- A download explorer opens.
- Click on "Corpora", search for "stopwords" and "wordnet" and download both.
- Furthermore, click on "Models",
- Search for "averaged_perceptron_tagger" and "punkt" and download both.
3. Run the program "LemmatizationFilePreprocessing.py"
