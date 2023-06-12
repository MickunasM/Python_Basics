#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:21:11 2023

Author: Marius Mickunas

Title: Logic, Control Flow and Filtering
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
< stricly less than
<= less than or euqal 
> strictly greater than
>= greater than or equal
== equal
!= not equal
'''
#%%
# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5*15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with an integer
print(True == 1)
#%%
# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print("test" <= y)

# Comparison of booleans
print(True > False)
#%%
# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)
#%%
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)
#%%
'''
Boolean operators with NumPy

Before, the operational operators like < and >= worked with NumPy arrays out of the box. Unfortunately, 
this is not true for the boolean operators and, or, and not.

To use these operators with NumPy, you will need np.logical_and(), np.logical_or() and np.logical_not()
'''

'''
Which areas in my_house are greater than 18.5 or smaller than 10?
Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, 
so that you can inspect the output.
'''
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))
#%%
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15 :
    print("big place!")
#%%
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")
#%%
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
#%%
# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
#%%
# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)
#%%
'''
Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.

Use cpc in combination with a comparison operator and 500. 
You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 
and False otherwise. Store this boolean Series as many_cars.

Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.

Print out car_maniac to see if you got it right.
'''

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]


# Print car_maniac
print(car_maniac)
#%%
# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)
#%%


