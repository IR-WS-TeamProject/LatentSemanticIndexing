# LatentSemanticIndexing by Team 3 (Hofman, Portisch, Ulbrich, Hentschel) 
Repository for Task 3 of the Information Retrival team project: Latent Semantic Indexing.

## General Information

Used Technologies:
- Python
- Libraries
    - Natural Language ToolKit (NLTK) for Python
    - Numpy, SciPy (v0.19)
    - json
- Webpage as UI build with Angular
- We recommend using Anaconda as package manager and runtime (https://www.continuum.io/downloads)

## How to Run

To learn the model please execute following steps:
1. Go to ``src/preprocessing/LemmatizationFilePreprocessing``
2. If you have never used the NLTK stopword removal list and the tokenizer, follow the subsequet steps. Otherwise continue with step 3.

 Execute 
 
    import nltk
    nltk.download()

- A download explorer opens.
- Click on "Corpora", search for "stopwords" and "wordnet" and download both.
- Furthermore, click on "Models",
- Search for "averaged_perceptron_tagger" and "punkt" and download both.

3. Copy the newsgroup folder into ``<project path>/20news-bydate`` , otherwise the server will not be able to locate the files
3. In the ``main`` method, set variable ``my_root_directory`` to the project path + ``/20news-bydate-train`` 
4. Run the program
5. Copy the generated BOW Dictionary into "src/files/" and name it "bow_lemmatization_train_data.dict"
6. [OPTIONAL] If you want to run the evalulation as well, please do the same process for the test data and copy the preprocessed BOW of test data in folder "src/files/" as well and name it "bow_lemmatization_test_data.dict"

To use the model and execute queries please follow these steps:
1. Learn the model as described above
2. Execute ``python /main.py``
3. Navigate to [http://localhost:8000](http://localhost:8000 "Localhost - Port 8000") in your web browser.
4. If successful, the user interface of the search should appear.
