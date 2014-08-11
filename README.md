# word\_game.py
A python script that performs a search for solutions to a word game and prints them.  The goal of the game is to find sets of five words that share an interchangeable vowel position.  E.g., one solution to the game would be the set of words:

    set(['last', 'lest', 'list', 'lost', 'lust'])

This set is a solution since the vowels `'a'`, `'e'`, `'i'`, `'o'`, and `'u'` occur in the same positions between the consonant clusters `'l'` and `'st'`.

# words.txt
A plain-text file listing English words, one per line.
Source: http://dreamsteep.com/component/docman/doc_download/3-the-english-open-word-list-eowl.html?Itemid=30

# solutions.txt
A plain-text file containing human-readable output of the python script with solutions written one-per line.