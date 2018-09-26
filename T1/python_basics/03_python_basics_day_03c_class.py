# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:19:32 2018

@author: arizai
"""

verse = """You may write me down in history
With your bitter, twisted lies,
You may trod me in the very dirt
But still, like dust, I'll rise.
"""

import random

#
#print text
##print text[5:40]
##print text.replace("\n", " ")
#
#print text.upper()
#
#print text.lower()
#
#print text[::-1]

#verse = verse.replace("e", "3")
#print verse.replace("l", "|_")

random_leet_ms = ["44", "|\/|", "^^", "MMMM"]

#print random.choice(random_leet_ms)

random_m = random.choice(random_leet_ms)

ems = verse.count("m")
print ems

#
#verse = verse.replace("m", random.choice(random_leet_ms), 1)
#verse = verse.replace("m", random.choice(random_leet_ms), 1)
#verse = verse.replace("m", random.choice(random_leet_ms), 1)
#verse = verse.replace("m", random.choice(random_leet_ms), 1)
#print verse

for i in range(ems+1):
    verse = verse.replace("m", random.choice(random_leet_ms), 1)
    print verse


#
#for char in verse:
#    #print char,
#    if char == "l":
#        #print "I got the L"
#        verse.replace(char,"|_")
#    print verse
#        
        
        
        
        
        
        
        
        
        
        