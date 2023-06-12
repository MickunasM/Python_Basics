#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:49:55 2023

Author: Marius Mickunas

Title: Writting your own functions
"""
#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tweets = pd.read_csv('https://assets.datacamp.com/production/repositories/463/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv', index_col = 0)

#%%
'''
Complete the function header by adding the appropriate function name, shout.
In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to shout_word.
Print the value of shout_word.
Call the shout function.
'''
# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()
#%%
'''
Complete the function header by adding the parameter name, word.
Assign the result of concatenating word with '!!!' to shout_word.
Print the value of shout_word.
Call the shout() function, passing to it the string, 'congratulations'.
'''
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')
#%%
'''
In the function body, concatenate the string in word with '!!!' and assign to shout_word.
Replace the print() statement with the appropriate return statement.
Call the shout() function, passing to it the string, 'congratulations', and assigning the call to the variable, yell.
To check if yell contains the value returned by shout(), print the value of yell.
'''
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return(shout_word)

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)
#%%
'''
You are now going to use what you've learned to modify the shout() function further. 
Here, you will modify shout() to accept two arguments. Parts of the function shout(), which you wrote earlier, are shown.
'''

'''
Modify the function header such that it accepts two parameters, word1 and word2, in that order.
Concatenate each of word1 and word2 with '!!!' and assign to shout1 and shout2, respectively.
Concatenate shout1 and shout2 together, in that order, and assign to new_shout.
Pass the strings 'congratulations' and 'you', in that order, to a call to shout(). Assign the return value to yell.
'''

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = (shout1 + shout2)

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)
#%%
nums = (3,4,6)

'''
Unpack nums to the variables num1, num2, and num3.
Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.
'''
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)
#%%
'''
In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. 
Here you will return multiple values from a function using tuples. 
Let's now update our shout() function to return multiple values. 
Instead of returning just one string, we will return two strings with the string !!! concatenated to each.
'''

'''
Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2, 
in that order.

Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.

Construct a tuple shout_words, composed of shout1 and shout2.

Call shout_all() with the strings 'congratulations' and 'you' and assign the result to yell1 and yell2 
(remember, shout_all() returns 2 variables!).
'''
# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)
#%%
'''
For this exercise, your goal is to recall how to load a dataset into a DataFrame. 
The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys 
are the names of languages and the values are the number of tweets in the given language. 
The file tweets.csv is available in your current directory.
'''

'''
Import the pandas package with the alias pd.
Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, 
add 1 to the value corresponding to this key in the dictionary, else add the key to langs_count and set the corresponding value to 1. 
Use the loop variable entry in your code.
'''
# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = tweets['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
         langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
#%%
'''
In this exercise, you will define a function with the functionality you developed in the previous exercise, 
return the resulting dictionary from within the function, and call the function with the appropriate arguments.
'''

'''
Define the function count_entries(), which has two parameters. 
The first parameter is df for the DataFrame and the second is col_name for the column name.

Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, 
add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.

Return the langs_count dictionary from inside the count_entries() function.

Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. 
Assign the result of the call to the variable result.
'''
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return(langs_count)

# Call count_entries(): result
result = count_entries(tweets, 'lang')

# Print the result
print(result)
#%%
