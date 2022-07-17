class unique_list(list):
	pass

L1 = [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14]  # len(L1) == 11

S1 = set(L1)
new_list = list(S1)
print(new_list)
# output:
# [0, 1, 3.14, 4, -90, 8.1, 9, 52.3, -6.1]


# Problem:
# elements of new list are not in the same order as 
# were in original list

# Algorithm
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

print(order)
print(len(order), len(new_list))

corrected_list = ['x']*len(L1)
print(corrected_list)

for value, index in order.items():
	print(index, value)
	corrected_list[index] = value

corrected_list = list(filter(lambda x: not isinstance(x, str), corrected_list))
print(corrected_list)