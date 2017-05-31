# LatentSemanticIndexing by Team 3 (Hofman, Portisch, Ulbrich, Hentschel) 
Repository for Task 3 of the Information Retrival team project: Latent Semantic Indexing.

## General Information

Used Technologies:
- Python and the Natural Language ToolKit (NLTK) for Pyton
- Webpage as UI build with Angular
- We recommend using Anaconda as package manager and runtime (https://www.continuum.io/downloads)

## Usage

To learn the model please execute following steps:
1. Go to src/preprocessing/LemmatizationFilePreprocessing
2. If you have never used the NLTK stopword removal list and the tokenizer:

 Execute 
 
    import nltk
    nltk.download()

- A download explorer opens.
- Click on "Corpora", search for "stopwords" and "wordnet" and download both.
- Furthermore, click on "Models",
- Search for "averaged_perceptron_tagger" and "punkt" and download both.

3. Copy the newsgroup folder into ``<project path>/20news-bydate-train`` , otherwise the server will not be able to locate the files
3. In the ``main`` method, set variable ``my_root_directory`` to the project path + ``/20news-bydate-train`` 
4. Run the program

To use the model and execute queries please follow these steps:
1. Learn the model as described above
2. Execute ``python /main.py``
3. Navigate to http:\\\\localhost:8000 in your web browser.
4. If successful, the user interface of the search should appear.
