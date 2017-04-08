import json
import re
from AbstractFilePreprocessing import AbstractFilePreprocessing
from nltk.stem import WordNetLemmatizer

class LemmatizationFilePreprocessing(AbstractFilePreprocessing):
    """This class offers bag of word (BOW) creation and can save the BOW to a file."""

    @staticmethod
    def stringTransformation(inputString):
        """This method transforms the input string into a BOW.
        It should also be used for the query transformation.
        """

        # initialize return structure and tokenize inputString
        transformedInput = []
        tokens = AbstractFilePreprocessing.tokenization(inputString)

        # initialize lemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        # TODO:  We need a POS tagger to determine whether the word is a noun or a verb
        #       (currently: everything is considered to be a noun when lemmatizing).


        # lemmatize
        for token in tokens:
            transformedInput.append(wordnet_lemmatizer.lemmatize(token, pos="n"))

        return transformedInput


    @staticmethod
    def saveBagOfWords(pathToCorpus, nameOfTargetFile):
        """This method reads the 20 newsgroup corpus, processes it, and writes the
            BOW to the specified file."""
        # dictionary for data structure: filepath -> BOW
        allFiles = LemmatizationFilePreprocessing.getPathsToAllResourceFiles(pathToCorpus)
        collection = {}

        # Loop over all files
        for file in allFiles:

            # open file, process content and add to dictionary
            with open(file, 'rt', encoding='utf-8', errors='replace') as f:
                print('Processing File ' + file)

                if pathToCorpus.endswith("test"):
                    # FOR TEST DATA
                    regexToGetNewFileName = "(?<=20news-bydate-test\\/)(.*)"

                if pathToCorpus.endswith("train"):
                    # FOR TRAIN DATA
                    # This regex will select the filename after 20news-bydate-train in the filepath;
                    # demasked: (?<=20news-bydate-train\/)(.*)
                    regexToGetNewFileName = "(?<=20news-bydate-train\\/)(.*)"

                regexer = re.search(regexToGetNewFileName, file)
                key = regexer.group(0)  # get filename
                data = f.read()
                value = LemmatizationFilePreprocessing.stringTransformation(data)
                collection[key] = value  # write filename (key) and BOW (value) into collection

        # save the dictionary
        with open(nameOfTargetFile, 'w+') as outfile:
            json.dump(collection, outfile)

        print("Number of files processed: " + str(len(collection)))
        print("Result saved in " + nameOfTargetFile)
        return collection


    @staticmethod
    def testing():
        """this method is just for testing purposes"""

        # testing the stringTransformation method
        testString = "I just love dogs and cats and playing with them."
        result = LemmatizationFilePreprocessing.stringTransformation(testString)
        print(result)

        # testing
        # myRootDirectory = "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/Information Retrieval and Web Search/Team Project/20news-bydate-train"
        # myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-test"
        # myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-train"
        myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-test"

        nameOfTargetFile = "bow_lemmatization_test_data.dict"

        # This process might take a while. If you already have a .dict file, you skip the following line.
        LemmatizationFilePreprocessing.saveBagOfWords(myRootDirectory, nameOfTargetFile)


LemmatizationFilePreprocessing.testing()
