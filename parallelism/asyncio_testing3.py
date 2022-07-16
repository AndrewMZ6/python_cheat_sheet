import asyncio
import time


async def f():
	print('Hey, this is function f() is executed')
	await asyncio.sleep(1)
	print('Hey, this is function f() is executed')

async def g():
	for i in range(5):
		print(f'counting {i}')
		time.sleep(1)
		# await asyncio.sleep(.3)


async def main():
	await asyncio.gather(f(), g())


if __name__ == '__main__':
	asyncio.run(main())