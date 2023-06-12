#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:20:12 2023

Author: Marius Mickunas

Title: Python Lists
"""
#%% Create list with different types

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

#%% List of lists As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

#%%
""" Indexing lists - use [] and put the number of the item in the list. 
Remeber python starts at 0 so if you wish to return the 7th item from the list you need to write list[6]. 
You can also use negative indexing - to return the last value in the list, use list[-1]

List slicing - list[3:5] this will give you the 4th item in the list and the 5th item, 
not the 6th becuase the number after the colon is exclusive, 
while the number before the colon is inclusive. Can also leave a number out of slicing - list[:5] will return everything from 0,1,2,3,4.
"""
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[4:6])

#%% Subset and calculate

""" 
After you've extracted values from a list, you can use them to perform additional calculations. 
Take this example, where the second and fourth element of a list x are extracted. 
The strings that result are pasted together using the + operator:

x = ["a", "b", "c", "d"] print(x[1] + x[3])
"""
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

#%% Slicing and dicing

"""
It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

my_list[start:end] The start index will be included, while the end index is not.
"""
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs - the first 6 elements
downstairs = areas[:6]

# Use slicing to create upstairs - the last 4 elements
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

#%% List manipulation - change, remove and add elements

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)

#%% Extend a list

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

#%% Inner workings of lists

""" 
Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

#%%







