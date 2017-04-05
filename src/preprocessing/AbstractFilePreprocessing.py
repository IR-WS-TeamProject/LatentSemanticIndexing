import os
import re
from nltk.corpus import stopwords


class AbstractFilePreprocessing:

    @staticmethod
    def string_transformation(inputString):
        pass

    @staticmethod
    def save_bag_of_words(pathToCorpus, nameOfTargetFile):
        pass

    # this method returns a string-array with the complete file paths for each file for further processing
    # it accepts the rootDirectory of the resource files (String format)
    @staticmethod
    def getPathsToAllResourceFiles(rootDirectory):
        # this is the root path where the news training data is located

        # get all subdirectories in pathToSourceDirectory
        subdirectories = [path for path in os.listdir(rootDirectory)
                          if os.path.isdir(os.path.join(rootDirectory, path))]

        # list with all files
        allFiles = []

        # get all files
        for directory in subdirectories:
            completePathToDirectory = rootDirectory + "/" + directory
            filesInDirectory = [file for file in os.listdir(completePathToDirectory)
                                if os.path.isfile(os.path.join(completePathToDirectory, file))]
            for file in filesInDirectory:
                completePathToFile = completePathToDirectory + "/" + file
                allFiles.append(completePathToFile)

        return allFiles

    # input: one string with the whole content
    # output: bag of words containing only charachters and with stopwords removed
    @staticmethod
    def tokenization(inputString):

        returnString = inputString.lower()

        # include all replace statements in this variable
        replaceVocabulary = {
            "from:": " ",
            "subject:": " ",
            "re:": "",
            "organization:": " ",
            "distribution:": " ",
            "lines:": " ",
            "reply-to:": " "
        }

        # replace headers
        returnString = AbstractFilePreprocessing.__multiple_replace__(returnString, replaceVocabulary)

        # only leave characters from a-z, numbers and other letters in there
        returnString = re.sub("[^a-z0-9üäößáàéè]", " ", returnString)

        # create tokens
        returnString = returnString.split(" ")

        # remove empty entries
        returnString = [x for x in returnString if x]

        # english stopword list
        stopWordList = set(stopwords.words('english'))
        # stopword removal
        returnString = [i for i in returnString if i not in stopWordList]

        return returnString

        # private method

    @staticmethod
    def __multiple_replace__(text, adict):
        rx = re.compile('|'.join(map(re.escape, adict)))

        def one_xlat(match):
            return adict[match.group(0)]

        return rx.sub(one_xlat, text)



