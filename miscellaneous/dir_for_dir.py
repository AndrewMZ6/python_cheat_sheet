# apply dir() function to list returned by dir function

def f():
	x = 10
	def inner(a):
		y = x + a
		print(y)

	return inner

c = f()

L = dir(c.__closure__)
for item in L:
 	print(f"for '{item}': \n", eval(f"dir(c.__closure__.{item})"), end='\n\n')
