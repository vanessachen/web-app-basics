'''
    get_mathdata.py

    This Python script opens the mathdata CSV file
    (built from the mathdata.db shelve) and creates a 
    LIST called `all_problems` which contains
    individual DICTIONARIES.

    Each dictionary represents one math problem.

'''

import csv

all_problems = []  # a LIST to contain math problem data

with open('csvmathdata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        all_problems.append(row)

# write your code below this line.
#  `all_problems` is a LIST of DICTIONARIES















# consider putting your data into a variable called 
# `user_results`
