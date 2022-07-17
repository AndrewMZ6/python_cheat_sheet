# tThe idea of the unique_list class
# is to add functionality to build-in class list
# that removes duplicates but saves the order of the 
# elements

# The first step is to create algorithm of how to
# filter duplicates and keep order

import sys
class unique_list(list):
	def __init__(self, x):
		super().__init__(x)
		# print(f"""x:\n
		# 		  {x}\n
		# 		  type:\n
		# 		  {type(x)}\n
		# 		  dir:\n
		# 		  {dir(x)}\n""")
		# print(f"""self:\n
		# 		  {self}\n
		# 		  type:\n
		# 		  {type(self)}\n
		# 		  dir:\n
		# 		  {dir(self)}\n""")

	def make_unique(self: list) -> list:
		S1 = set(self)
		new_list = list(S1)

		order = dict()
		for element in new_list:
			if element not in order:
				order[element] = L1.index(element)

		corrected_list = ['x']*len(L1)


		for value, index in order.items():
			corrected_list[index] = value

		corrected_list = list(filter(lambda x: not isinstance(x, str), corrected_list))

		# check if the correction is right:
		# to make sure that corrected list didn't remove some elements from the original
		#     if all unique elements of the original list 
		# 	  are present in corrected list then the correction
		# 	  made right
		# 
		# 	OR
		# 
		# 	if set of original list and set of corrected list are equal

		assert set(self) == set(corrected_list), "The number of unique elements does not match"

		return corrected_list







L1 = [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14, 'x']  # len(L1) == 11

print(unique_list(L1).make_unique())
sys.exit()

print(f"original list:\n{L1}")
S1 = set(L1)
new_list = list(S1)
print(f"new_list:\n{new_list}")

# output:
# [0, 1, 3.14, 4, -90, 8.1, 9, 52.3, -6.1]


# Problem:
# elements of new list are not in the same order as 
# were in original list L1

# Algorithm:
# order = dict()
# for element in new_list:
# 	ind = check what was the index of the element in the original list
#	
#	check if order dict already contains the element as a key
#	
#   add key/value pair to the order dictionary where key is the element
#	and value is it's index in the original list
#	
# 	create zeroed list of length len(order)
# 	for value, index in order.items()
#	place into zeroed list at index index the value
#   	WARNING! since len(order) is less than len(L1)
# 		some indexes are get out of range! For example
# 		3.14 in the original list L1 had index 9, but new zeroed list's
# 		max index is 8

order = dict()
for element in new_list:
	if element not in order:
		order[element] = L1.index(element)

print(f"order dict:\n{order}")


corrected_list = ['x']*len(L1)


for value, index in order.items():
	corrected_list[index] = value

corrected_list = list(filter(lambda x: not isinstance(x, str), corrected_list))
print(f"corrected_list:\n{corrected_list}")


# OUTPUT: 
# original list:
# [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14]
# new_list:
# [0, 1, 3.14, 4, -90, 8.1, 9, 52.3, -6.1]
# order dict:
# {0: 5, 1: 0, 3.14: 9, 4: 7, -90: 6, 8.1: 1, 9: 2, 52.3: 3, -6.1: 4}
# corrected_list:
# [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 3.14]
# [Finished in 148ms]