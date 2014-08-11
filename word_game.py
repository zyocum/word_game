__author__ = "Zachary Yocum"
__email__  = "zyocum@brandeis.edu"

"""
This program performs a search for solutions to a word game and prints them.

The goal of the game is to find sets of five words that share an interchangeable vowel position.

E.g., one solution to the game would be the set:

    set(['last', 'lest', 'list', 'lost', 'lust'])

This is a valid solution since the vowels 'a', 'e', 'i', 'o', and 'u' can each 
replace the underscore in the skeleton 'l_st' to form a word.
"""

import os

vowels = 'aeiou' # Exclude 'y' since it can't make up its mind if it's a vowel
with open(os.path.join(os.getcwd(), 'words.txt'), 'r') as words_file:
    words = words_file.read().strip().split('\n')
    words_file.close()
del words_file # We don't need this file once the words list is in memory

def skeletons(word):
    """Given a word, this function returns a generator of word skeleton strings
such that each individual vowel character in the word is replaced with an
underscore.
E.g., skeletons('skeleton') -> ['sk_leton', 'skel_ton', 'skelet_n']"""
    # Replace the vowel at index i with an underscore in the word
    skeletonize = lambda i : word[:i] + '_' + word[i+1:]
    # Test whether the character c is a vowel
    is_vowel = lambda c : c in vowels
    return (skeletonize(i) for i, c in enumerate(word) if is_vowel(c))

def print_solutions(words):
    """This is the main function that runs the nested loops necessary to find
solutions to the game and print them as they are discovered. The dictionary is
keyed on word skeletons and the values are sets of words that can be
constructed by filling in the underscore in the key with a vowel.
    I.e., {'Eb_uche' : set(['Ebauche']),
           ...
           '_dult'   : set(['adult']),
           ...
           'h_ll'    : set(['hall', 'hell', 'hill', 'hull']),
           ...
           'l_st'    : set(['last', 'lest', 'list', 'lost', 'lust']),
           ...
           'zyth_m'  : set(['zythum'])}"""
    dictionary = {}
    # Iterate over all words
    for word in words:
        # Iterate over word skeletons (to use as dictionary keys)
        for key in skeletons(word):
            # Test if the key already exists
            if not dictionary.get(key):
                # If not, add the key-value pair
                dictionary[key] = set([word])
            else:
                # If so, add the word to the candidate solution set
                dictionary[key].add(word)
                # Test if a solution is found, and if so print it
                if len(dictionary[key]) == len(vowels):
                    print(', '.join(sorted(dictionary[key])))

if __name__ == '__main__':
    print_solutions(words)