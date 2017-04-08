""" import statements """
import json
import re
from nltk.stem import WordNetLemmatizer
# if a syntax error is shown, right click the preprocessing directory and mark as source
from .AbstractFilePreprocessing import AbstractFilePreprocessing


class LemmatizationFilePreprocessing(AbstractFilePreprocessing):
    """ This class implements lemmatization and is based on an abstract method. """

    @staticmethod
    def string_transformation(input_string):
        """ This method returns a string array with the words of the document.
            It needs to be used for query preprocessing as well. """

        # initialize return structure and tokenize inputString
        transformed_input = []
        tokens = AbstractFilePreprocessing.tokenization(input_string)

        # initialize lemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        #        We need a POS tagger to determine whether the word is a noun or a verb
        #       (currently: everything is considered to be a noun when lemmatizing).


        # lemmatize
        for token in tokens:
            transformed_input.append(wordnet_lemmatizer.lemmatize(token, pos="n"))

        return transformed_input


    @staticmethod
    def save_bag_of_words(path_to_corpus, name_of_target_file):
        """This method reads the 20 newsgroup corpus, processes it, and writes the
            BOW to the specified file."""
        # dictionary for data structure: filepath -> BOW
        all_files = AbstractFilePreprocessing.__get_paths_to_resource_files__(path_to_corpus)
        collection = {}

        # Loop over all files
        for file in all_files:

            # open file, process content and add to dictionary
            with open(file, 'rt', encoding='utf-8', errors='replace') as file:
                print('Processing File ' + file)

                if path_to_corpus.endswith("test"):
                    # FOR TEST DATA
                    regex_to_get_new_file_name = "(?<=20news-bydate-test\\/)(.*)"

                if path_to_corpus.endswith("train"):
                    # FOR TRAIN DATA
                    # This regex will select the filename after 20news-bydate-train in the filepath;
                    # demasked: (?<=20news-bydate-train\/)(.*)
                    regex_to_get_new_file_name = "(?<=20news-bydate-train\\/)(.*)"

                regexer = re.search(regex_to_get_new_file_name, file)
                key = regexer.group(0)  # get filename
                data = file.read()
                value = LemmatizationFilePreprocessing.string_transformation(data)
                collection[key] = value  # write filename (key) and BOW (value) into collection

        # save the dictionary
        with open(name_of_target_file, 'w+') as outfile:
            json.dump(collection, outfile)

        print("Number of files processed: " + str(len(collection)))
        print("Result saved in " + name_of_target_file)
        return collection


    @staticmethod
    def testing():
        """this method is just for testing purposes"""

        # my_root_directory = "/Users/alexandrahofmann/Documents/Master Uni MA/2. Semester/" \
        #                    "Information Retrieval and Web Search/Team Project/20news-bydate-train"
        my_root_directory = "C:/Users/D060249/Documents/Mannheim/Semester 2/" \
                            "Information Retrieval and Web Search/IR Team Project/" \
                            "20news-bydate-train"

        name_of_target_file = "bow_lemmatization_test_data.dict"

        # This process might take a while.
        # If you already have a .dict file, you skip the following line.
        LemmatizationFilePreprocessing.save_bag_of_words(my_root_directory, name_of_target_file)

        # testing the stringTransformation method
        test_string = "I just love dogs and cats and playing with them."
        result = LemmatizationFilePreprocessing.string_transformation(test_string)
        print(result)


LemmatizationFilePreprocessing.testing()
