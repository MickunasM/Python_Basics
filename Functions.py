#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 27 21:46:31 2023

Author: Marius Mickunas

Title: Functions

A function is a piece of re-usable code, that you can call on anytime e.g. print(), max(), round(1.68, 1), help(function_name)
"""

#%%
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

print(out2)

#%% Multiple arguments

""" 
Use + to merge the contents of first and second into a new list: full.
Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
Finish off by printing out full_sorted.
"""
help(sorted)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)


#%% Methods
"""
Methods are functions that belong to objects
e.g. capitalize(), replace(), bit_lenght(), conjugate(), index(), count()

"""
#%% String Methods

"""
Strings come with a bunch of methods. Follow the instructions closely to discover some of them. 
If you want to discover them in more detail, you can always type help(str).
"""
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place) 
print(place_up)

# Print out the number of o's in place
print(place.count('o'))

#%% List Methods
"""
index(), to get the index of the first element of a list that matches its input and
count(), to get the number of times an element appears in a list.
"""
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

#%% List Methods (2)

""" 
Most list methods will change the list they're called on. Examples are:

append(), that adds an element to the list it is called on,
remove(), that removes the first element of a list that matches the input, and
reverse(), that reverses the order of the elements in the list it is called on.
"""
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5); areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

#%% Packages
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

#%%
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

#%%
