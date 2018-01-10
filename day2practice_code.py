'''
    day2practice_code.py
    Practice code for Day 2

    A program to deliver a text-based version
    of the quiz app.
'''


from day1vocabulary import items_to_learn
import shelve

study_items = shelve.open("items.db")
item_results = shelve.open("results.db")

# YOUR JOB:
# take the items from items_to_learn and put them
# into the shelve called study_items one at a time.


for item in items_to_learn.keys():
    item_results[item] = []

for item in items_to_learn.keys():
    definition = items_to_learn[item]
    print("******")
    print(definition)

    # get input from the user and save it into
    # a variable called `guess` (which is always a STRING)
    guess = input("type your guess >  ")


    # check whether the user answered correctly
    # record the result into the item_results shelve
    if guess == item:
        print("You are correct")
        item_results[item] = "correct"
    elif guess != item:
        print("Incorrect, this is the word: '{}'".format(item))
        item_results[item] = "study more"


# loop over the items in item_results
# and figure out which ones the user needs to practice.
for item in items_to_learn.keys():
    if item_results[item]=="correct":
        print("These are the terms you answered correctly: {}".format(item))
    elif item_results[item]=="study more":
        print("These are the terms you answered incorrectly: {}".format(item))
        study_items[item] = item
# Then display a summary to the user (using `print()` )
print ("These are the items to study: {}".format(study_items))


# don't forget to close the shelves!!
study_items.close()
item_results.close()
