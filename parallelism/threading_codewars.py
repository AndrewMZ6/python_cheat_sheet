# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
# solving codewars kata using threads
import threading
import time
from faker import Faker

ipv4_gen = Faker()
customers = [ipv4_gen.ipv4() for _ in range(20)]


# customers = [2,2,3,3,4,4]
n = 3
index = 0
def handle():
	name = threading.currentThread().getName()
	global customers
	thread_list = []
	global index
	iteration_number = 0
	while index < len(customers):
		print(f"[{name}]-> iteration_number: {iteration_number}")
		print(f"[{name}]-> current index: {index}")
		t = customers[index]
		print(f"[{name}]-> index of appended element: {customers.index(t)}")
		thread_list.append(t)
		print(f"[{name}]-> current thread_list: {thread_list}\n")
		index += 1
		iteration_number += 1
		time.sleep(1)
	print(f"[{name}]-> final thread_list: {thread_list}")
	return thread_list

def queue_time(customers, n):
	name_gen = Faker()
	thread_names = [name_gen.word() for _ in range(n)]
	threads = [threading.Thread(target=handle, name=uwu.capitalize()) for uwu in thread_names]
	for thread in threads:
		thread.start()
		# time.sleep(0.25)

	for thread in threads:
		thread.join()

queue_time(customers, n)