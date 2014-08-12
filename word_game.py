__author__ = "Zachary Yocum"
__email__  = "zyocum@brandeis.edu"

"""This program performs a search for solutions to a word game and prints them.

The goal of the game is to find sets of five words that share an 
interchangeable vowel position.

E.g., one solution to the game would be the set:

    set(['last', 'lest', 'list', 'lost', 'lust'])

This is a valid solution since the vowels 'a', 'e', 'i', 'o', and 'u' can each 
replace the underscore in the skeleton 'l_st' to form a word."""

def skeletons(word):
    """Generates all skeletons of a word by replacing vowels with underscores.
    
    E.g.: skeletons('skeleton') -> ['sk_leton', 'skel_ton', 'skelet_n']"""
    # Replace the vowel at index i with an underscore in the word
    skeletonize = lambda i : word[:i] + '_' + word[i+1:]
    # Test whether the character c is a vowel
    is_vowel = lambda c : c.lower() in vowels
    return (skeletonize(i) for i, c in enumerate(word) if is_vowel(c))

def print_solutions(words):
    """Searches for solutions to the game and prints them as they are found."""
    # When the iteration over the words is completed:
    # dictionary = {
    #     ...
    #     '_dult'  : set(['adult']),
    #     ...
    #     'h_ll'   : set(['hall', 'hell', 'hill', 'hull']),
    #     ...
    #     'l_st'   : set(['last', 'lest', 'list', 'lost', 'lust']),
    #     ...
    #     'zyth_m' : set(['zythum'])
    # }
    from collections import defaultdict
    dictionary = defaultdict(set)
    # Iterate over all words
    for word in words:
        # Iterate over word skeletons (to use as dictionary keys)
        for skeleton in skeletons(word):
            # Add the word to the candidate solution set for the skeleton
            dictionary[skeleton].add(word)
            # Test if the candidate solution set is valid, and print it if so
            if len(dictionary[skeleton]) == len(vowels):
                print(', '.join(sorted(dictionary[skeleton])))

if __name__ == '__main__':
    # Exclude 'y' from vowels since it can't make up its mind if it's a vowel
    vowels = 'aeiou'
    # Open and parse the words file to create the words list
    with open('words.txt', 'r') as words_file:
        words = words_file.read().strip().split('\n')
    # Search the words list for solutions and print them
    print_solutions(words)