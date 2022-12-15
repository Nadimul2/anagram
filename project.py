import random
import collections
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class AnagramFinder():
    
    def __init__(self, file_name, word):
        # Takes file name and word to seach in the file
        # Returns a dataframe with anagrams as well as frequency
        # Searches the word in the file and returns word + anagrams with frequency
        self.file_name = file_name
        self.word = word
    
        

    def file_open(self):
        # Open file and read the contents and convert them to a list. Removes puntuation marks
        # returns a clean list of words.
        with open(self.file_name, '+r') as word:
            text = word.read().split(' ')
            text = [i.replace('\n\n', '').replace('\n','').replace(".",'').replace(':','') for i in text]
        return text
    
    
    def anagram_dict(self, text):
        #Input: list of words
        #Output: dictionary with letters as keys and words+ anagrams as values
        grouped_anagrams = {}
        # iterating over the list to group all anagrams
        for string in text:
            sorted_string = str(sorted(string))
            if sorted_string in grouped_anagrams:
                grouped_anagrams[sorted_string].append(string)
            else:
                grouped_anagrams[sorted_string] = [string]
        return grouped_anagrams
    
    def anagram_freq(self, dic):
        #Takes a dictionary as input and returns the frequency of each values
        #Append the values and frequency to a dataframe
        df = pd.DataFrame()
        values = dic.values()
        anagrams = {}
        for words in values:
            anagram = set(words)
            count = len(words)
            df = df.append({'Anagrams': anagram, 'Frequency': count}, ignore_index=True)
        return df
    
    def search(self, dic):
        #Takes a dictionary as input and returns the word in the dictionary along with its frequency
        for value in dic.values():
            if self.word in value:
                return set(value), len(value)
        return 'Word not in file'
     
        
def main():
    """Test function for the program"""
    a = AnagramFinder('words.txt', 'no')
    text = a.file_open()
    dic = a.anagram_dict(text)
    freq = a.anagram_freq(dic)
    search = a.search(dic)
    print(freq)
    print(search)

    

if __name__ == "__main__":
    main()   