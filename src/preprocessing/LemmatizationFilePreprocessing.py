""" import statements """
import json
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
# if a syntax error is shown, right click the preprocessing directory and mark as source
from preprocessing.AbstractFilePreprocessing import AbstractFilePreprocessing


class LemmatizationFilePreprocessing(AbstractFilePreprocessing):
    """ This class implements lemmatization and is based on an abstract method. """

    @staticmethod
    def string_transformation(input_string):
        """ This method returns a string array with the words of the document.
            It needs to be used for query preprocessing as well. """

        transformed_input = []

        # tokenize words
        tokenized_string = nltk.word_tokenize(input_string)

        # POS tagging
        pos_tagged_tokens = nltk.pos_tag(tokenized_string)

        # initialize lemmatizer
        wordnet_lemmatizer = WordNetLemmatizer()

        # lemmatize
        for pos_tagged_token in pos_tagged_tokens:
            word, part_of_speech = pos_tagged_token

            if str(part_of_speech).startswith("N"):
                #token is a noun
                transformed_input.append(wordnet_lemmatizer.lemmatize(word, pos=wordnet.NOUN))

            elif str(part_of_speech).startswith("V"):
                #token is a verb
                transformed_input.append(wordnet_lemmatizer.lemmatize(word, pos=wordnet.VERB))

            elif str(part_of_speech).startswith("J"):
                #token is an adjective
                transformed_input.append(wordnet_lemmatizer.lemmatize(word, pos=wordnet.ADJ))

            elif str(part_of_speech).startswith("R"):
                #token is adverb
                #note: lemmatizer does not handle adverbs

                extended_adverb = word + ".r.1"

                # handle the exception that no lemma is found
                try:
                    lemmas = wordnet.synset(extended_adverb).lemmas()
                    lemmatized_adverb = lemmas[0].pertainyms()[0].name()
                except (IndexError, AttributeError, nltk.corpus.reader.wordnet.WordNetError):
                    lemmatized_adverb = word

                # add base form
                transformed_input.append(lemmatized_adverb)

            else:
                #token is not tagged -> simply add token
                transformed_input.append(word)

        # initialize return structure
        return_structure = []

        # delete everything except characters
        for token in transformed_input:
            # replace with empty string
            return_structure.append(re.sub("[^a-züäößáàéè]", "", str(token).lower()))

            # remove empty entries
            return_structure = [x for x in return_structure if x]

        # english stopword list
        stopword_list = set(stopwords.words('english'))

        # stopword removal
        return_structure = [i for i in return_structure if i not in stopword_list]

        return return_structure


    @staticmethod
    def save_bag_of_words(path_to_corpus, name_of_target_file):
        """This method reads the 20 newsgroup corpus, processes it, and writes the
            BOW to the specified file."""
        # dictionary for data structure: filepath -> BOW
        all_files = AbstractFilePreprocessing.__get_paths_to_resource_files__(path_to_corpus)
        collection = {}

        # Loop over all files
        for file_path in all_files:

            # open file, process content and add to dictionary
            with open(file_path, 'rt', encoding='utf-8', errors='replace') as file:
                print('Processing File ' + file_path)

                if path_to_corpus.endswith("test"):
                    # FOR TEST DATA
                    regex_to_get_new_file_name = "(?<=20news-bydate-test\\/)(.*)"

                if path_to_corpus.endswith("train"):
                    # FOR TRAIN DATA
                    # This regex will select the filename after 20news-bydate-train in the filepath;
                    # demasked: (?<=20news-bydate-train\/)(.*)
                    regex_to_get_new_file_name = "(?<=20news-bydate-train\\/)(.*)"

                regexer = re.search(regex_to_get_new_file_name, file_path)
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
                            "20news-bydate-test"

        name_of_target_file = "bow_lemmatization_test_data.dict"

        # This process might take a while.
        # If you already have a .dict file, you skip the following line.
        LemmatizationFilePreprocessing.save_bag_of_words(my_root_directory, name_of_target_file)

        # testing the stringTransformation method
        test_string = "I just love dogs and cats and playing with them. 123I love it :)" \
                      "He enjoys my jokes - that's what makes it so special to me."
        result = LemmatizationFilePreprocessing.string_transformation(test_string)
        print(result)


LemmatizationFilePreprocessing.testing()
