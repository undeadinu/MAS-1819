# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:44:29 2018

@author: arizai
"""

# =============================================================================
#
# strings
# slicing
# simple programs (iteration, comparison, find)
#
# =============================================================================

import string

# strings
# compound data type >>> access to parts

my_string = "drawing"
print my_string

print

print type(my_string)

print

# [] operator
print my_string[0]
print my_string[-1]

# for loop
for letter in my_string:
    print letter,
    # print letter

    # print letter,
    # print letter

print

# traversal
index = 0
while index < len(my_string):
    # print index
    letter = my_string[index]
    print letter,
    index += 1

print

# list comprehension
letters_in_my_string = [aletter for aletter in my_string]
print letters_in_my_string

print


# back traverse function
def back_traverse(my_string):
    for letter in my_string[::-1]:
        print letter,


# function call
back_traverse("aeiou")

print

# built-in functions
# reversed()
for letter in reversed("aeiou"):
    print letter,

print("")

# str(), list()
print 41
print "41"
print type(41)
print type("41")
print type(str(41))
print list("41")
print list(reversed(my_string))

print

# slicing
print my_string[:]
print my_string[0:]
print my_string[:4]  
# start, stop, stride
print my_string[::-1]

print

# operations on strings
answer = 41+1
print answer
# wrong_answer = "41" + 1
wrong_answer = "41" + "1"
print wrong_answer
print my_string*3
print ("A " + my_string + " ") * 3

# string methods
print my_string.capitalize()
print my_string.upper()
my_string_upper = my_string.upper()
print my_string_upper
print my_string

print

# split
song = "This is a mellow song..."
song_list = song.split()
print song_list

# join
print " ".join(song_list)

print

# concatenation
my_string = "A description of a drawing"
purpose = " it's informative"
print my_string + purpose


# simple programs
# iteration
def countdown(n):
    while n >= 0:
        if n == 0:
            print("End!")
        else:
            print n,
        n -= 1

countdown(20)

print

# comparison
def compare_food(food_a, food_b):
    if food_a == food_b:
        print "The same"
    else:
        print food_a + " and " + food_b + " are not quite the same"


compare_food("pears", "apples")


def alphabetical_order(string_a, string_b):
    if string_a > string_b:
        print string_b + " then " + string_a
    else:
        print string_a + " then " + string_b



alphabetical_order("pears", "grapes")

print


# find
def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1


my_string = "drawing"
print find(my_string, "w")
print my_string.find("w")

# raw_input
input_user = raw_input("Write something: ")
print input_user
