import os

class AbstractFilePreprocessing:


    def stringTransformation(inputString):
        pass

    def saveBOW(pathToCorpus):
        pass

    # this method returns a string-array with the complete file paths for each file for further processing
    # it accepts the rootDirectory of the resource files (String format)
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

    def __str__(self):
        return str(self.id)



