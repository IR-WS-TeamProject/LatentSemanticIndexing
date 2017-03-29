import os.path


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



# example of how to call the method
myRootDirectory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-train"
allFiles = getPathsToAllResourceFiles(myRootDirectory)
print (allFiles) # print all files

# Read the first file as a single string and output
with open(allFiles[0], 'rt') as f:
    data = f.read()
    print(data)


################################################################
# Next steps
# 1) write a "bag of words" method that accepts a string
#    - delete punctuation [Problems: Telephone numbers e.g. (716) 837-2475 and times e.g. 11:57:19 and prices e.g. $4.95]
#    - toLowerCase
#    - stem (use external library)
#    - tokenize [Problems: Numbers that belong together e.g. 071 831 7723]
