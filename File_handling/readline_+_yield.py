# first create a txt file and write fake emails there
from faker import Faker

fk = Faker()

with open('mytext.txt', 'w') as fd:
	for i in range(50):
		fd.write("%s\n" % fk.ascii_email())

-----------------------------------------------------------
# now read the file 
filename = 'mytext.txt'

def get_line(filename):

	with open(filename, 'r') as fd:
		s = 1
		k = 0
		
		while s:
			k += 1
			print(f'starting to read line number {k}')
			s = fd.readline().rstrip('\n')
			yield s
			

	print(f"file closed status: {fd.closed}")

g = get_line(filename)

try:
	while True:
		print(next(g))
except StopIteration:
		pass

print('program execution proceeds')

starting to read line number 1
# douglasfrye@yahoo.com
# starting to read line number 2
# michael76@yahoo.com
# starting to read line number 3
# matthewsbrandon@yahoo.com
# starting to read line number 4
# sanchezmark@fitzgerald.biz
# starting to read line number 5
# angela53@wolfe.org
# starting to read line number 6
# paul34@gmail.com
# starting to read line number 7
# simmonsashley@gmail.com
# starting to read line number 8
# jonesruth@gmail.com
# starting to read line number 9
# kayla52@gmail.com
# starting to read line number 10
# stephanie45@baldwin.com
# starting to read line number 11
# cordovanicholas@taylor-bailey.biz
# starting to read line number 12
# hernandezmichael@jacobs.org
# starting to read line number 13
# hansonrachael@hotmail.com
# starting to read line number 14
# davidbenitez@hotmail.com
# starting to read line number 15
# vnicholson@stone-griffin.biz
# starting to read line number 16
# oblack@davis.org
# starting to read line number 17
# othompson@hall.com
# starting to read line number 18
# lgriffith@johnson.com
# starting to read line number 19
# todd98@garcia-griffin.com
# starting to read line number 20
# tnguyen@hotmail.com
# starting to read line number 21
# andrewsimpson@hotmail.com
# starting to read line number 22
# birdnicholas@gmail.com
# starting to read line number 23
# stacy92@price.biz
# starting to read line number 24
# watkinsalan@yahoo.com
# starting to read line number 25
# williamvalencia@hotmail.com
# starting to read line number 26
# davidbruce@gmail.com
# starting to read line number 27
# reneebaker@burch.com
# starting to read line number 28
# wwalker@hotmail.com
# starting to read line number 29
# arthur57@yahoo.com
# starting to read line number 30
# mclaughlinedward@gmail.com
# starting to read line number 31
# xmiller@yahoo.com
# starting to read line number 32
# linda63@gmail.com
# starting to read line number 33
# charlesmay@hotmail.com
# starting to read line number 34
# john88@leon.net
# starting to read line number 35
# elizabethnorris@gmail.com
# starting to read line number 36
# cory08@gmail.com
# starting to read line number 37
# vhernandez@ali-dickson.org
# starting to read line number 38
# jasonmiller@turner.com
# starting to read line number 39
# brussell@yahoo.com
# starting to read line number 40
# jamesstrong@sullivan-ruiz.com
# starting to read line number 41
# dakota28@gmail.com
# starting to read line number 42
# katie32@byrd-manning.info
# starting to read line number 43
# valenciamary@hotmail.com
# starting to read line number 44
# lisabishop@yahoo.com
# starting to read line number 45
# randygillespie@gmail.com
# starting to read line number 46
# mckinneykevin@garza-eaton.com
# starting to read line number 47
# lloydmary@douglas-mckinney.net
# starting to read line number 48
# judy31@yahoo.com
# starting to read line number 49
# kromero@delgado-cardenas.com
# starting to read line number 50
# guzmandestiny@sanford-gordon.org
# starting to read line number 51

# file closed status: True
# program execution proceeds
