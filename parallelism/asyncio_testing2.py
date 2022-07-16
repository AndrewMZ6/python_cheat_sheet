# The purpose was to run 2 functions asynchronously with random sleep time
# just to see how does it works

import random
import string as s
import asyncio
from sys import exit

async def numbers():
	for num in range(20):
		print(num)
		await asyncio.sleep((1+random.random())**2 - 1)
	return 'numbers finished successfully'

async def alpha():
	for letter in s.ascii_lowercase:
		print(letter)
		await asyncio.sleep((1+random.random())**2 - 1)
	return 'numbers finished successfully'

async def main():
	res = await asyncio.gather(numbers(), alpha())
	print(res)

if __name__ == '__main__':
	asyncio.run(main())

# Output:
# 
# 0
# a
# b
# 1
# c
# 2
# 3
# d
# 4
# e
# f
# 5
# g
# h
# 6
# 7
# i
# j
# k
# l
# 8
# m
# 9
# 10
# 11
# n
# o
# 12
# 13
# p
# 14
# q
# 15
# r
# 16
# s
# 17
# t
# u
# 18
# v
# 19
# w
# x
# y
# z
# ['numbers finished successfully', 'numbers finished successfully']
# [Finished in 37.9s]
