#!/usr/bin/env python3
"""This program performs a search for solutions to a word game and prints them.

The goal of the game is to find sets of five words that share an 
interchangeable vowel position.

E.g., one solution to the game would be the set:

    {'last', 'lest', 'list', 'lost', 'lust'}

This is a valid solution since the vowels 'a', 'e', 'i', 'o', and 'u' can each 
replace the underscore in the skeleton 'l_st' to form a word."""

__author__ = "Zachary Yocum"
__email__  = "zyocum@brandeis.edu"

from collections import defaultdict

# Exclude 'y' from vowels since it can't make up its mind if it's a vowel
VOWELS = 'aeiou'
MASK = '_'

def is_vowel(c):
    """Predicate to test if a character is a vowel."""
    return c.lower() in VOWELS

def skeletonize(word, i):
    """Skeletonizes a word by replacing the i-th character with a mask."""
    skeleton = MASK.join((word[:i], word[i+1:]))
    return skeleton

def skeletons(word):
    """Generates all skeletons of a word by replacing vowels with underscores.
    
    E.g.: skeletons('skeleton') -> ['sk_leton', 'skel_ton', 'skelet_n']"""
    return (skeletonize(word, i) for i, c in enumerate(word) if is_vowel(c))

def solutions(words):
    """Search for and generate solutions to the game as they are found."""
    dictionary = defaultdict(set)
    for word in words:
        for skeleton in skeletons(word):
            dictionary[skeleton].add(word)
            if len(dictionary[skeleton]) == len(VOWELS):
                yield ', '.join(sorted(dictionary[skeleton]))

def main(wordsfile='words.txt'):
    with open(wordsfile, 'r') as file:
        words = file.read().splitlines()
    for solution in solutions(words):
        print(solution)

if __name__ == '__main__':
    main()