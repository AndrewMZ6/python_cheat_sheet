# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

import asyncio
import time

def queue_time(customers, n):
    start = time.time()   
    
    async def coro():
        nonlocal customers
        while customers:
            t = customers.pop(0)
            await asyncio.sleep(t)
    
    tasks = (coro() for _ in range(n))
    
    async def main():
        await asyncio.gather(*tasks)
        
    asyncio.run(main())
    
    stop = time.time()    
    
    return int(stop - start)

print(queue_time([], 1))			# expected 0
print(queue_time([5], 1))			# expected 5
print(queue_time([2], 5))			# expected 2 
print(queue_time([1,2,3,4,5], 1))	# expected 15
print(queue_time([1,2,3,4,5], 100))	# expected 5 
print(queue_time([2,2,3,3,4,4], 2))	# expected 9 

# OUTPUT:
# 0
# 5
# 2
# 15
# 4			wrong answer here
# 9
# [Finished in 36.3s]