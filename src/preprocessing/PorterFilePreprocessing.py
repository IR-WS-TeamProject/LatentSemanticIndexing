from AbstractFilePreprocessing import AbstractFilePreprocessing # if a syntax error is shown, right click the preprocessing directory and mark as source
from nltk.stem.porter import *
import json
import nltk # this is required in order to be able to download the stopword list


class PorterFilePreprocessing(AbstractFilePreprocessing):

    @staticmethod
    def multiple_replace(text, adict):
        rx = re.compile('|'.join(map(re.escape, adict)))
        def one_xlat(match):
            return adict[match.group(0)]
        return rx.sub(one_xlat, text)


    # this method returns a string array with the words of the document
    # it needs to be used for query preprocessing as well
    @staticmethod
    def stringTransformation(inputString):

        returnString = AbstractFilePreprocessing.tokenization(inputString)

        # porter stemmer
        stemmer = PorterStemmer()

        # Stopword Removal and Stemming
        # Remarks: the current nltk porter stemmer has some known issues with "oed"
        newReturnString = []
        for currentToken in returnString:
            if currentToken != "oed" and currentToken != "aing":  # porter stemmer cannot handle that

                stemmer.stem(currentToken)
                newReturnString.append(currentToken)

            elif currentToken == "oed": # add oed without stemming
                newReturnString.append("oed")

            elif currentToken == "aing":
                newReturnString.append("aing")

        returnString = newReturnString

        return returnString

    @staticmethod
    def saveBagOfWords(pathToCorpus, nameOfTargetFile):
        # dictionary for data structure: filepath -> BOW
        allFiles = PorterFilePreprocessing.getPathsToAllResourceFiles(pathToCorpus)
        collection = {}

        # Loop over all files
        for file in allFiles:

            # open file, process content and add to dictionary
            with open(file, 'rt', encoding='utf-8', errors='replace') as f:
                print('Processing File ' + file)
                regexToGetNewFileName = "(?<=20news-bydate-train\\/)(.*)" # This regex will select the filename after 20news-bydate-train in the filepath; demasked: (?<=20news-bydate-train\/)(.*)
                regexer = re.search(regexToGetNewFileName, file)
                key = regexer.group(0) # get filename
                data = f.read()
                value = PorterFilePreprocessing.stringTransformation(data)
                collection[key] = value # write filename (key) and BOW (value) into collection

        # save the dictionary
        with open(nameOfTargetFile, 'w+') as outfile:
            json.dump(collection, outfile)

        print("Number of files processed: " + str(len(collection)) )
        print("Result saved in bow_porter.dict")
        return collection

    @staticmethod
    def testing():
        # myRootDirectory = "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/Information Retrieval and Web Search/Team Project/20news-bydate-train"
        myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-train"

        nameOfTargetFile = "bow_porter.dict"

        # This process might take a while. If you already have a .dict file, you skip the following line.
        PorterFilePreprocessing.saveBagOfWords(myRootDirectory, nameOfTargetFile)

        # Example Query String Transformation
        print(PorterFilePreprocessing.stringTransformation("Hello World, this is my Query!"))


#################################################################################################################
# Execute Preprocessing
#################################################################################################################


# IMPORTANT:
# When used first, you have to download the stopword list.
# Therefore, uncomment the following line and execute.
# A download explorer opens. Click on "Corpora", search for "stopwords" and download only the stopwords list.
# nltk.download()

# PorterFilePreprocessing.testing()



