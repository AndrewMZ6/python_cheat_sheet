# tThe idea of the unique_list class
# is to add functionality to build-in class list
# that removes duplicates but saves the order of the 
# elements

# The first step is to create algorithm of how to
# filter duplicates and keep order

import sys
class unique_list(list):
	print(__doc__)
	def __init__(self, x):
		super().__init__(x)
		# print(f"""x:\n
		# 		  {super()}\n
		# 		  type:\n
		# 		  {type(super())}\n
		# 		  dir:\n
		# 		  {dir(super())}\n""")
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


L1 = [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14]  # add 'x' element that will be removed

print(unique_list(L1).make_unique())


# OUTPUT:
# x:

# 				  [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14, 'x']

# 				  type:

# 				  <class 'list'>

# 				  dir:

# 				  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# self:

# 				  [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14, 'x']

# 				  type:

# 				  <class '__main__.unique_list'>

# 				  dir:

# 				  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'make_unique', 'pop', 'remove', 'reverse', 'sort']

# Traceback (most recent call last):
#   line 60, in <module>
#     print(unique_list(L1).make_unique())
#   line 53, in make_unique
#     assert set(self) == set(corrected_list), "The number of unique elements does not match"
# AssertionError: The number of unique elements does not match
# [Finished in 152ms]