""" import statements """
import os
import re
from nltk.corpus import stopwords


class AbstractFilePreprocessing:
    """ abstract class for preprocessing """


    @staticmethod
    def string_transformation(input_string):
        """ Performs a string transformation on a string object with stemming/lemmatization. """
        pass


    @staticmethod
    def save_bag_of_words(path_to_corpus, name_of_target_file):
        """ Creates a dictionary as data structure: filepath -> bag of words. """
        pass


    @staticmethod
    def tokenization(input_string):
        """ input: one string with the whole content
            output: bag of words containing only charachters and with stopwords removed """

        return_string = input_string.lower()

        # include all replace statements in this variable
        vocabulary = {
            "from:": " ",
            "subject:": " ",
            "re:": "",
            "organization:": " ",
            "distribution:": " ",
            "lines:": " ",
            "reply-to:": " "
        }

        # replace headers
        return_string = AbstractFilePreprocessing.__multiple_replace__(return_string, vocabulary)

        # only leave characters from a-z, numbers and other letters in there
        return_string = re.sub("[^a-z0-9üäößáàéè]", " ", return_string)

        # create tokens
        return_string = return_string.split(" ")

        # remove empty entries
        return_string = [x for x in return_string if x]

        # english stopword list
        stopword_list = set(stopwords.words('english'))

        # stopword removal
        return_string = [i for i in return_string if i not in stopword_list]

        return return_string


    # private methods

    @staticmethod
    def __get_paths_to_resource_files__(root_directory):
        """ This method returns a string-array with complete file paths for each file.
            It accepts the rootDirectory of the resource files (String format). """

        # get all subdirectories in pathToSourceDirectory
        subdirectories = [path for path in os.listdir(root_directory)
                          if os.path.isdir(os.path.join(root_directory, path))]

        # list with all files
        all_files = []

        # get all files
        for directory in subdirectories:
            complete_path_to_directory = root_directory + "/" + directory
            files_in_directory = [file for file in os.listdir(complete_path_to_directory)
                                  if os.path.isfile(os.path.join(complete_path_to_directory, file))]
            for file in files_in_directory:
                complete_path_to_file = complete_path_to_directory + "/" + file
                all_files.append(complete_path_to_file)

        return all_files


    @staticmethod
    def __multiple_replace__(text, adictionary):
        """ input: text where occurrences specified in the input dictionary will be replaced
            output: string with replaced parts """

        word = re.compile('|'.join(map(re.escape, adictionary)))

        def get_match(match):
            """ return match of dictionary array """
            return adictionary[match.group(0)]

        return word.sub(get_match, text)
