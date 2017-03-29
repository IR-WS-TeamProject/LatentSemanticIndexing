import os.path
import re
from nltk.stem.porter import *


# this method returns a string-array with the complete file paths for each file for further processing
# it accepts the rootDirectory of the resource files (String format)
def getPathsToAllResourceFiles (rootDirectory):
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



def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)



################################################################
# Next steps
# 1) write a "bag of words" method that accepts a string
#    - delete punctuation [Problems: Telephone numbers e.g. (716) 837-2475 and times e.g. 11:57:19 and prices e.g. $4.95] -> started
#    - toLowerCase -> DONE
#    - stem (use external library)
#    - tokenize [Problems: Numbers that belong together e.g. 071 831 7723] -> started
################################################################


# this method returns a string array with the words of the document
def getBagOfWords(inputString):

    # does it really work like this? Do I have to cast the input Parameter?! I hate this ducktyping...
    returnString = str(inputString)

    # lower case transformation
    returnString = returnString.lower()

    # TODO: how to handle special characters etc. ?!?!
    # TODO: Cover all ASCII special characters (not that many)

    #------------------------------------------------------------------

    # very cumbersome and not performant, but one way would be:
    returnString = ''.join(i for i in returnString if ord(i) < 128) # this limits the allowed characters to ASCI II

    adict = {
        "from:": "",
        "subject:": "",
        "re:": "",
        "organization:": "",
        "distribution:": "",
        "lines:": "",
        "reply-to:": "",

        ": ": " ",              # allows for tokens like "12:00:30"
        ". ": " ",              # allows for tokens like "10.50" or dates like "2017.03.05"
        ", ": " ",              # allows for tokens like 5,5 (German decimal)

        "\n": " ",              # handle line breaks
        ".\n": " ",
        "..": " ",
        ",\n": " ",
        ":\n": " ",

        "!": "",                # ascii 33
        '\"': "",               # ascii 34: quotation marks
        "#": "",                # ascii 35
        "$": "",                # ascii 36
        "%": "",                # ascii 37
        "&": "",                # ascii 38
        "\'": "",               # ascii 39: single quote
        "(": "",                # ascii 40
        ")": "",                # ascii 41
        "*": "",                # ascii 42
        "+": "",                # ascii 43
        "-": "",                # ascii 45
        "/": "",                # ascii 47

        ";": "",                # ascii 59
        "<": "",                # ascii 60
        "=": "",                # ascii 61
        ">": "",                # ascii 62
        "?": "",                # ascii 63

        "[": "",                # ascii 91
        "\\": "",               # ascii 92
        "]": "",                # ascii 93
        "^": "",                # ascii 94
        "_": "",                # ascii 95
        "`": "",                # ascii 96

        "{": "",                # ascii 123
        "|": "",                # ascii 124
        "}": "",                # ascii 125
        "~": ""                 # ascii 126
    }

    returnString = multiple_replace(returnString, adict)

    #------------------------------------------------------------------

    # create tokens
    returnString = returnString.split(" ")

    #remove empty entries
    returnString = [x for x in returnString if x]


    # apply stemming by porter
    stemmer = PorterStemmer()
    words = [stemmer.stem(x) for x in returnString]

    returnString = ' '.join(words)

    # create tokens
    returnString = returnString.split(" ")

    return returnString


# example of how to call the method
myRootDirectory = "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/Information Retrieval and Web Search/Team Project/20news-bydate-train"
allFiles = getPathsToAllResourceFiles(myRootDirectory)
# print (allFiles) # print all files

# Read the first file as a single string and output
with open(allFiles[0], 'rt', encoding='utf-8', errors='replace') as f:
    data = f.read()
    print(data)
    print ("BOW:")
    print(getBagOfWords(data))