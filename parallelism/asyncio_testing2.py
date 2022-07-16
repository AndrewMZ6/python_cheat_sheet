import random
import asyncio
from faker import Faker

# asynchronous fake email generator
async def email_gen(x):
	print('-> email_gen first line')
	emails = Faker()
	while x:
		x -= 1
		yield emails.email()

# asynchronous random number [0.0, 1.0) generator
async def mygen(x):
	print('-> mygen first line')
	while x:
		x -= 1
		yield random.random()

# prints random numbers in async for loop
async def f(x):
	print('-> f() first line')
	async for i in mygen(x):
			print(i)
			await asyncio.sleep(1)

# prints emails in async for loop
async def h(x):
	print('-> h() first line')
	async for j in email_gen(x):
			print(j)
			await asyncio.sleep(1)

# main coroutine
async def main():
	await asyncio.gather(f(4), h(3))

# creates eventloop and runs the main coroutine
if __name__ == '__main__':
	asyncio.run(main())

# output:
#
# -> f() first line
# -> mygen first line
# 0.007900825453143523
# -> h() first line
# -> email_gen first line
# julie81@example.net
# 0.9710039284381164
# kelly89@example.net
# 0.5811082916136737
# ojones@example.org
# 0.2650784122835159
# [Finished in 4.5s]