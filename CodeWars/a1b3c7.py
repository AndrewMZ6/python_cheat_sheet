def func(s:str) ->str:

	counter = 1
	m = ''
	
	try:
		for i in range(len(s)):
			if s[i] == s[i+1]:
				counter += 1
			else:
				m = m + str(s[i]) + str(counter)
				counter = 1

	except IndexError:
			m = m + s[i] + str(counter)

	return m


p = func('aacbbbttbc asssssssdas')
print(p)
