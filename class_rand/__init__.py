import pandas as pd
import numpy as np

# import os
# file = input('file: ');
# filename, file_extension = os.path.splitext(file)
# if filename != 'webarchive' or 'txt':

with open('/Users/diego/Documents/LambdaUnit3/words.webarchive') as inpt:
    dictionary = inpt.read()
    words = dictionary.splitlines()

class Random():

    """
    x = Random(words)

    For dataframe with custom shape,
    input a variable inplace of entire words dictionary like so:
        
    first -> data = x.select_words_range(100)
    then -> make_df_rows(10, data)
    shape would be: (100, 1)

    alternatively, input entire words dictionary (25,486 words) -> make_df_rows(10)
    shape would be: (100, 255)
    """

    def __init__(self, words):
        self.words = words
        
    def select_words_range(self, number_of_words, first_word_number=0, last_word_number=None):
        """
        select number of words in combination and range. 
        there are 25,486 words. Words starting with L will fall somewhere around 12,000
        """
        numbers = []
        sentence = []
        if last_word_number == None:
            last_word_number = len(self.words)
            for i in range(0, number_of_words):
                numbers.append(np.random.randint(first_word_number, last_word_number))
            for i in numbers:
                sentence.append(self.words[i])
            return " ".join(sentence)

    def make_df_rows(self, rows, words=None):
        """
        select rows for words list
        """
        if words == None:
            data_for_df = np.array_split(self.words, rows)
            return pd.DataFrame(data=data_for_df)
        else:
            word = words.split(" ")
            data_for_df = np.array_split(word, rows)
            return pd.DataFrame(data=data_for_df)

# -----------------

# attempt to give user more freedom to input dif files of words


# import pandas as pd
# import numpy as np
# import os

# file = input('file: ');
# filename, file_extension = os.path.splitext(file)

# if filename != 'webarchive' or 'txt':
#     with open('/Users/diego/Documents/LambdaUnit3/classes/words.webarchive') as inpt:
#         dictionary = inpt.read()
#         words = dictionary.splitlines()
        
#         else:
#             with open(file) as inpt:
#                 dictionary = inpt.read()
#                 words = dictionary.splitlines()
                
#                 class Random():
                    
#                     def __init__(self, words):
#                     self.words = words
                    
#                     def select_words_range(self, number_of_words, first_word_number=0, last_word_number=None):
#                         numbers = []
#                         sentence = []
#                         if last_word_number == None:
#                             last_word_number = len(self.words)
#                             for i in range(0, number_of_words):
#                                 numbers.append(np.random.randint(first_word_number, last_word_number))
#                             for i in numbers:
#                                 sentence.append(self.words[i])
#                             return " ".join(sentence)
                            
#                     def make_df_rows(self, rows):
#                         data_for_df = np.array_split(self.words, rows)
#                         df = pd.DataFrame(data=data_for_df)
#                         return df