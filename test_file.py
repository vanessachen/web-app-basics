'''
    test_file.py

    A file to open the mathdata.db shelve
    and export its data in CSV format.
    NOTE: this code strips out the metadata.
    The resulting CSV file only contains problem data.
'''

import csv
import shelve

one_session = shelve.open("mathdata")

problems = one_session["all_problems"]

with open('csvmathdata.csv', 'w') as csvfile:
    fieldnames = ["operand1", "operator", "operand2", "correct", "start_time", "end_time", "user_guess"]
    #fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # create the header row

    for prob in problems:
        writer.writerow(prob)


one_session.close()












