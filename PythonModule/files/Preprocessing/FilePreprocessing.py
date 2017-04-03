import os.path
import json
from nltk.stem.porter import *
from nltk.corpus import stopwords
import nltk



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



# this method returns a string array with the words of the document
# it needs to be used for query preprocessing as well
def stringTransformation(inputString):

    # does it really work like this? Do I have to cast the input Parameter?! I hate this ducktyping...
    returnString = str(inputString)

    # lower case transformation
    returnString = returnString.lower()


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
        ".\"" : " ",
        ".\'" : " ",
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

    # delete/replace special characters
    returnString = multiple_replace(returnString, adict)

    # create tokens
    returnString = returnString.split(" ")

    #remove empty entries
    returnString = [x for x in returnString if x]

    #stopword list
    stopWordList = set(stopwords.words('english'))

    # porter stemmer
    stemmer = PorterStemmer()

    # Stopword Removal and Stemming
    # Remarks: the current nltk porter stemmer has some known issues with "oed"
    newReturnString = []
    for currentToken in returnString:
        if (currentToken not in stopWordList) and currentToken != "oed": #porter stemmer cannot handle that

            # handling cases when the last character is a '.' (this should not be the case but causes an exception with the stemmer)
            if currentToken.endswith("."):
                currentToken = currentToken[:len(currentToken) - 1]

            # print(currentToken)
            stemmer.stem(currentToken)
            newReturnString.append(currentToken)

        elif currentToken == "oed": # add oed without stemming
            newReturnString.append("oed")

    returnString = newReturnString

    return returnString



def getAndSaveBagOfWordForAllFiles(pathToCorpus):
    # dictionary for data structure: filepath -> BOW
    allFiles = getPathsToAllResourceFiles(pathToCorpus)
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
            value = stringTransformation(data)
            collection[key] = value # write filename (key) and BOW (value) into collection

    print("Number of files processed: " + len(collection))

    # save the dictionary
    with open('bow_porter.dict', 'w+') as outfile:
        json.dump(collection, outfile)

    return collection




#################################################################################################################
# Execute Preprocessing
#################################################################################################################


# IMPORTANT: When used first, you have to download the stopword list. Therefore, uncomment the following line and execute. Download only the stowords list.
# nltk.download()

# "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/Information Retrieval and Web Search/Team Project/20news-bydate-train"
myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-train"

# This process might take a while. If you already have a .dict file, you skip the following line.
getAndSaveBagOfWordForAllFiles(myRootDirectory)

# Example Query String Transformation
print(stringTransformation("Hello World, this is my Query!"))




