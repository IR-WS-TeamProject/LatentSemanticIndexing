""" import statements """
import re
import json
# import porter stemmer
from nltk.stem import porter
# if a syntax error is shown, right click the preprocessing directory and mark as source
from .AbstractFilePreprocessing import AbstractFilePreprocessing


class PorterFilePreprocessing(AbstractFilePreprocessing):
    """ This class implements porter stemming and is based on an abstract method """


    @staticmethod
    def string_transformation(input_string):
        """ This method returns a string array with the words of the document.
            It needs to be used for query preprocessing as well. """

        return_string = AbstractFilePreprocessing.tokenization(input_string)

        # porter stemmer
        stemmer = porter.PorterStemmer()

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
        """ creates a dictionary as data structure: filepath -> bag of words """

        all_files = AbstractFilePreprocessing.__get_paths_to_resource_files__(path_to_corpus)
        collection = {}

        # Loop over all files
        for file_path in all_files:
            # open file_path, process content and add to dictionary
            with open(file_path, 'rt', encoding='utf-8', errors='replace') as file:
                print('Processing File ' + file_path)
                # This regex will select the filename after 20news-bydate-train in the filepath;
                # demasked: (?<=20news-bydate-train\/)(.*)
                regex_to_get_new_file_name = "(?<=20news-bydate-train\\/)(.*)"
                regexer = re.search(regex_to_get_new_file_name, file_path)
                key = regexer.group(0)  # get filename
                data = file.read()
                value = PorterFilePreprocessing.string_transformation(data)
                collection[key] = value  # write filename (key) and BOW (value) into collection

        # save the dictionary
        with open(name_of_target_file, 'w+') as outfile:
            json.dump(collection, outfile)

        print("Number of files processed: " + str(len(collection)))
        print("Result saved in bow_porter.dict")
        return collection

    @staticmethod
    def testing():
        """ method used for testing purposes """

        my_root_directory = "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/" \
                            "Information Retrieval and Web Search/Team Project/20news-bydate-train"
        # my_root_directory = "C:/Users/D060249/Documents/Mannheim/Semester 2/" \
        #             "Information Retrieval and Web Search/IR Team Project/20news-bydate-train"

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
