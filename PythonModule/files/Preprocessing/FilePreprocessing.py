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

    #------------------------------------------------------------------

    # very cumbersome and not performant, but one way would be:
    returnString = ''.join(i for i in returnString if ord(i) < 128) # this limits the allowed characters to ASCI II

    # exclude header parameters
    returnString = returnString.replace("from:", "")
    returnString = returnString.replace("subject:", "")
    returnString = returnString.replace("re:", "")
    returnString = returnString.replace("organization:", "")
    returnString = returnString.replace("distribution:", "")
    returnString = returnString.replace("lines:", "")
    returnString = returnString.replace("reply-to:", "")


    # take care of special characters...
    returnString = returnString.replace(": ", " ")  # allows for tokens like "12:00:30"
    returnString = returnString.replace(". ", " ")  # allows for tokens like "10.50" or dates like "2017.03.05"
    returnString = returnString.replace(", ", " ")  # allows for tokens like 5,5 (German decimal)

    returnString = returnString.replace("", "")     # ascii 32: space
    returnString = returnString.replace("!", "")    # ascii 33
    returnString = returnString.replace('\"', "")   # ascii 34: quotation marks
    returnString = returnString.replace("#", "")    # ascii 35
    returnString = returnString.replace("$", "")    # ascii 36
    returnString = returnString.replace("%", "")    # ascii 37
    returnString = returnString.replace("&", "")    # ascii 38
    returnString = returnString.replace("\'", "")   # ascii 39: single quote
    returnString = returnString.replace("(", "")    # ascii 40
    returnString = returnString.replace(")", "")    # ascii 41
    returnString = returnString.replace("*", "")    # ascii 42
    returnString = returnString.replace("+", "")    # ascii 43
    returnString = returnString.replace("-", "")    # ascii 45
    returnString = returnString.replace("/", "")   # ascii 47

    returnString = returnString.replace(";", "")    # ascii 59
    returnString = returnString.replace("<", "")    # ascii 60
    returnString = returnString.replace("=", "")    # ascii 61
    returnString = returnString.replace(">", "")    # ascii 62
    returnString = returnString.replace("?", "")    # ascii 63

    returnString = returnString.replace("[", "")    # ascii 91
    returnString = returnString.replace("\\", "")   # ascii 92
    returnString = returnString.replace("]", "")    # ascii 93
    returnString = returnString.replace("", "")     # ascii 94
    #returnString = returnString.replace("_", "")   # ascii 95

    returnString = returnString.replace("{", "")    # ascii 123
    returnString = returnString.replace("|", "")    # ascii 124
    returnString = returnString.replace("}", "")    # ascii 125
    returnString = returnString.replace("~", "")    # ascii 126

    # TODO: Cover all ASCII special characters (not that many)

    #------------------------------------------------------------------


    #handle line breaks
    returnString = returnString.replace("\n", " ")

    # create tokens
    returnString = returnString.split(" ")

    #remove empty entries
    returnString = [x for x in returnString if x]

    return returnString




# example of how to call the method
myRootDirectory = "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/Information Retrieval and Web Search/Team Project/20news-bydate-train"
allFiles = getPathsToAllResourceFiles(myRootDirectory)
# print (allFiles) # print all files

# Read the first file as a single string and output
with open(allFiles[0], 'rt') as f:
    data = f.read()
    print(data)
    print ("BOW:")
    print(getBagOfWords(data))

