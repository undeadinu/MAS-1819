# adapted from Pig Latin exercise (MIT 6.149: Introduction to Python 2015)

######################################
### Pig-CHDE validity check helper ###
######################################

# Ask the user for a word; print whether the word
# is a valid pig-CHDE version of a word in word_list,
# which is a list of strings



"""
Basic Pig-CHDE rules
1. if word starts with "k" > replace "k" with "ch"
2. if word ends in consonant > add a random vowel at the end of the word
3. all words end with -li

Test cases:    
english word > Pig-CHDE word
kilo > chiloli
kitten > chittenali, chitteneli, chittenili, chittenoli or chittenuli
sugar > sugarali, sugareli, sugarili, sugaroli or sugaruli
cookie > cookieli

Test your code with the above Pig-CHDE words, any of these should output:
"This is a valid version Pig-CHDE word"
or extra points (reconstruct original english word):
"This is a valid version Pig-CHDE word of the english word _______"

Also test your code with the following not valid Pig-CHDE words:
kylobiteli, balloonli, backpack
all these should return:
"This is not a valid Pig-CHDE word"

Hints:
- Ask the user to input a word
- You may assume that the user inputs a word of only letters
- You may not assume that the input is all lowercase
- Use what you have learned:
- Check for conditions with if, elif, else...
- Check for inclusion of a string in a list with the in keyword
- Check for inclusion of a string in a another string with the in keyword
- Check for comparison with == or !=
- Use slicing to access parts of strings

The file words.txt should be saved in the same folder where you are running your code

"""


