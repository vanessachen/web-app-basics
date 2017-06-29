'''
	math_session.py

	A file to open the mathdata.db shelve
	which contains data from a single math session.
'''

import shelve

one_session = shelve.open("mathdata")

for key in one_session:
	if key == "all_problems":

		# your code goes here. Hint: See page 6 of the handout.

		pass


one_session.close()