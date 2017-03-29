import os.path
import string


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



################################################################
# Next steps
# 1) write a "bag of words" method that accepts a string
#    - delete punctuation [Problems: Telephone numbers e.g. (716) 837-2475 and times e.g. 11:57:19 and prices e.g. $4.95]
#    - toLowerCase
#    - stem (use external library)
#    - tokenize [Problems: Numbers that belong together e.g. 071 831 7723]
################################################################


def getBagOfWords(inputString):

    # does it really work like this? Do I have to cast the input Parameter?! I hate this ducktyping...
    returnString = str(inputString)
    returnString = returnString.lower()

    # TODO: how to handle special characters etc. ?!?!

    """
        # very cumbersome and not performant, but one way would be:
        returnString = ''.join(i for i in returnString if ord(i) < 128) # this limits the allowed characters to ASCI II
        
        # take care of special characters...
        returnString = returnString.replace(": ", "")
        returnString = returnString.replace(". ", "")
        returnString = returnString.replace(", ", "")
        returnString = returnString.replace("(", "")
        returnString = returnSTring.replace(")", "")
    """

    #handle line breaks
    returnString = returnString.replace("\n", " ")

    # create tokens
    returnString = returnString.split(" ")

    #remove empty entries
    returnString = [x for x in returnString if x]

    return returnString


# example of how to call the method
myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-train"
allFiles = getPathsToAllResourceFiles(myRootDirectory)
print (allFiles) # print all files

# Read the first file as a single string and output
with open(allFiles[0], 'rt') as f:
    data = f.read()
    print(getBagOfWords(data))

