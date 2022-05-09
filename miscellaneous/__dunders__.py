class myclass:
	'''
		This class is one of the foremost classes that's everseen. Pog?

	'''

	__name__ = 'SPARTA'

	def __init__(self, value:str) -> object:
		self.value = value
		self.dic: dict = {}

	def __eq__(self, other: object) -> bool:

		try:
			assert hasattr(other, 'value') == True and type(other.value) == str
			return len(self.value) == len(other.value)
		except AssertionError:
			print('LOL')

	def __hash__(self):
		return 91231


	def __getitem__(self, key):
		return self.dic[key]

	def __setitem__(self, key, value):
		self.dic[key] = value

	def __call__(self):
		pass
		print('Ooooooooopsie')
    
    
    

m = myclass('word')
n = myclass('word')
z = myclass(54)

print(m == n)
print(m == z)

print(hash(m))

m[0] = 51
m[9] = 'hello'

print(m.dic)
