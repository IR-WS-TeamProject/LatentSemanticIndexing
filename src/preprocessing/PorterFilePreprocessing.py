from nltk.stem.porter import *
# if a syntax error is shown, right click the preprocessing directory and mark as source
from .AbstractFilePreprocessing import AbstractFilePreprocessing
import json
# this is required in order to be able to download the stopword list
import nltk


class PorterFilePreprocessing(AbstractFilePreprocessing):

    # this method returns a string array with the words of the document
    # it needs to be used for query preprocessing as well
    @staticmethod
    def string_transformation(input_string):

        return_string = AbstractFilePreprocessing.tokenization(input_string)

        # porter stemmer
        stemmer = PorterStemmer()

        # Stopword Removal and Stemming
        # Remarks: the current nltk porter stemmer has some known issues with "oed"
        new_return_string = []
        for current_token in return_string:
            # porter stemmer cannot handle those terms
            if current_token != "oed" and current_token != "aing":

                stemmer.stem(current_token)
                new_return_string.append(current_token)

            # add words without stemming
            elif current_token == "oed":
                new_return_string.append("oed")
            elif current_token == "aing":
                new_return_string.append("aing")

        return_string = new_return_string

        return return_string

    @staticmethod
    def save_bag_of_words(path_to_corpus, name_of_target_file):
        # dictionary for data structure: filepath -> BOW
        all_files = PorterFilePreprocessing.getPathsToAllResourceFiles(path_to_corpus)
        collection = {}

        # Loop over all files
        for file in all_files:

            # open file, process content and add to dictionary
            with open(file, 'rt', encoding='utf-8', errors='replace') as f:
                print('Processing File ' + file)
                # This regex will select the filename after 20news-bydate-train in the filepath;
                # demasked: (?<=20news-bydate-train\/)(.*)
                regex_to_get_new_file_name = "(?<=20news-bydate-train\\/)(.*)"
                regexer = re.search(regex_to_get_new_file_name, file)
                key = regexer.group(0) # get filename
                data = f.read()
                value = PorterFilePreprocessing.string_transformation(data)
                collection[key] = value # write filename (key) and BOW (value) into collection

        # save the dictionary
        with open(name_of_target_file, 'w+') as outfile:
            json.dump(collection, outfile)

        print("Number of files processed: " + str(len(collection)))
        print("Result saved in bow_porter.dict")
        return collection

    @staticmethod
    def testing():
        # my_root_directory = "/Users/alexandrahofmann/Documents/Master Uni MA/
        # 2. Semester/Information Retrieval and Web Search/Team Project/20news-bydate-train"
        my_root_directory = "C:/Users/D060249/Documents/Mannheim/Semester 2/Information Retrieval and Web Search/IR Team Project/20news-bydate-train"

        name_of_target_file = "bow_porter.dict"

        # This process might take a while.
        # If you already have a .dict file, you skip the following line.
        PorterFilePreprocessing.save_bag_of_words(my_root_directory, name_of_target_file)

        # Example Query String Transformation
        print(PorterFilePreprocessing.
              string_transformation("Hello World, this is my Query!"))


######################################################################
# Execute Preprocessing
######################################################################


# IMPORTANT:
# When used first, you have to download the stopword list.
# Therefore, uncomment the following line and execute.
# A download explorer opens. Click on "Corpora",
# search for "stopwords" and download only the stopwords list.
# nltk.download()

# PorterFilePreprocessing.testing()



