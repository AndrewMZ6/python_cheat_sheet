# The purpose was to run 2 functions asynchronously with random sleep time
# just to see how does it works

# hint: The keyword "await" passes function control back to the event loop

import random
import string as s
import asyncio
from sys import exit
from time import sleep

async def blocking():
	for i in range(10):
		print(i)
		sleep(.1)

# the function "numbers" suspends and awaits for function "blocking" to finish
# then the execution proceeds
async def numbers():
	print("----------------1----------")
	res = await blocking()
	print("----------------2----------")
	return 'numbers finished successfully'

async def main():
	res = await asyncio.gather(numbers())
	print(res)

if __name__ == '__main__':
	asyncio.run(main())


# output:
# ----------------1----------
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# ----------------2----------
# ['numbers finished successfully']
# [Finished in 1.3s]
