# adapted from Pig Latin exercise (MIT 6.149: Introduction to Python 2015)

import string
import random

WORDLIST_FILENAME = "words.txt"

"""
you don't need to understand the next helper code
"""

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

word_list = loadWords()

"""
end of helper code
"""

###########################
### English-to-Pig-CHDE ###
###########################

# welcome to Pig-CHDE

# convert the word to Pig-CHDE

vowels = ["a", "e", "i", "o", "u"]

word_to_convert = "love"

print "word to convert is:", word_to_convert

# Pig-CHDE rules
if word_to_convert[0] == "k":
    # print "word starts with k"
    word_converted = "ch" + word_to_convert[1:]
    # print "so we replace the k with ch"
    if word_to_convert[-1] not in vowels:
        # print "the is no vowel at the end"
        random_vowel = random.choice(vowels)
        # print "so we add a random vowel"
        word_converted = word_converted + random_vowel
    # print "we finally make it small"
    word_converted = word_converted + "li"
    print "The Pig-CHDE version of the word", word_to_convert, "is", word_converted
else:
    # print "it does not start with k"
    if word_to_convert[-1] not in vowels:
        # print "the is no vowel at the end"
        random_vowel = random.choice(vowels)
        word_converted = word_to_convert + random_vowel
    word_converted = word_to_convert + "li"
    print "The Pig-CHDE version of the word", word_to_convert, "is", word_converted


###############################
### Pig-CHDE validity check ###
###############################

# Ask the user for a word; print whether the word
# is a valid pig-CHDE version of a word in word_list,
# which is a list of strings

# YOUR CODE HERE

        
