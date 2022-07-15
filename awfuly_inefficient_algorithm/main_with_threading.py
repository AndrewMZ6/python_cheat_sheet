from threading import Thread
from func_module import my_gen

L = []

def thr1():
	for i in my_gen(30):
		L.append(f"t1::{i}")
	print("thread 1 done!")

def thr2():
	for j in my_gen(30):
		L.append(f"t2::{j}")
	print("thread 2 done!")

def main_thr():
	for k in my_gen(40):
		L.append(f"mt::{k}")
	print("main thread done!")

t1 = Thread(target=thr1)
t2 = Thread(target=thr2)

t1.start()
t2.start()
main_thr()

print(len(L))

# output:
# thread 1 done!
# thread 2 done!
# main thread done!
# 100
# [Finished in 6.5s]
