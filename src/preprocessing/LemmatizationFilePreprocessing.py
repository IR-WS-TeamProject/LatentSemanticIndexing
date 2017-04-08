""" import statements """
# if a syntax error is shown, right click the preprocessing directory and mark as source
from .AbstractFilePreprocessing import AbstractFilePreprocessing

class LemmatizationFilePreprocessing(AbstractFilePreprocessing):
    """ This class implements lemmatization and is based on an abstract method """


    @staticmethod
    def string_transformation(input_string):
        """ This method returns a string array with the words of the document.
            It needs to be used for query preprocessing as well. """
        ...


    @staticmethod
    def save_bag_of_words(path_to_corpus, name_of_target_file):
        """ Creates a dictionary as data structure: filepath -> bag of words. """
        ...
