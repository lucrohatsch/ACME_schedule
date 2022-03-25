"""
This script is he solution for the "junior software developer" exercise.
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

"""

from functions import getData, tranformData, processData

lines = getData('.\data\input.txt')
persons, days = tranformData(lines)
peers= processData(persons, days)




print(f"{'Employees pair':<18} -> {'Days':<2}")
for x in peers:
    print(f"{f'{x[0]} - {x[1]}':<18} -> {x[2]:<2}") 

