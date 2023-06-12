#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 22:22:43 2023

Author: Marius Mickunas

Title: Loops
"""

#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gapminder = pd.read_csv('https://assets.datacamp.com/production/repositories/287/datasets/5b1e4356f9fa5b5ce32e9bd2b75c777284819cca/gapminder.csv', index_col=0)
cars = pd.read_csv('https://assets.datacamp.com/production/repositories/287/datasets/79b3c22c47a2f45a800c62cae39035ff2ea4e609/cars.csv', index_col=0)
brics = pd.read_csv('https://assets.datacamp.com/production/repositories/287/datasets/b60fb5bdbeb4e4ab0545c485d351e6ff5428a155/brics.csv', index_col=0)

#%%
'''
Create the variable offset with an initial value of 8.
Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
Print out the sentence "correcting...".
Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
Finally, still within your loop, print out offset so you can see how it changes.
'''
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)
#%%
'''
Inside the while loop, complete the if-else statement:
If offset is greater than zero, you should decrease offset by 1.
Else, you should increase offset by 1.
'''
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)
#%%
'''
Write a for loop that iterates over all elements of the areas list and prints out every element separately.
'''
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for values in areas:
    print(values)
#%%
'''
Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
Update the print() statement so that on each run, a line of the form "room x: y" should be printed, 
where x is the index of the list element and y is the actual list element, i.e. the area. 
Make sure to print out this exact string, with the correct spacing.
'''
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, values in enumerate(areas) :
    print("room" + str(index) + ":" + str(values))
#%%
'''
Adapt the print() function in the for loop so that the first printout becomes "room 1: 11.25", 
the second one "room 2: 18.0" and so on.
'''
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))
#%%
'''
Write a for loop that goes through each sublist of house and prints out the x is y sqm, 
where x is the name of the room and y is the area of the room.
'''
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house :
    print("the " + x[0] + " is " + str(x[1]) + " sqm")
#%%
'''
Write a for loop that goes through each key:value pair of europe. 
On each iteration, "the capital of x is y" should be printed out, where x is the key and y is the value of the pair.
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + str(value))
#%%
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
np_height = np.array(height)

# For loop over np_baseball
for values in np.nditer(np_baseball):
    print(values)
    
# For loop over np_height
for values in np.nditer(np_height):
    print(str(values) + " inches")
#%%
'''
Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: 
one to print out the row label and one to print out all of the rows contents.
'''

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
#%%
'''
Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", 
the second iteration "AUS: 731", and so on.
The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.
'''
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
#%%
'''
Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. 
You can use the string method upper() for this.
To see if your code worked, print out cars. 
Don't indent this code, so that it's not part of the for loop
'''
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = (row["country"].upper())

# Print cars
print(cars)
#%%
'''
Replace the for loop with a one-liner that uses .apply(str.upper). 
The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
As usual, print out cars to see the fruits of your hard labor
'''
# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
#%%

#%%

#%%

#%%

#%%

#%%

#%%