
import tkinter as tk
from tkinter import ttk
import time 
import threading

flag = False

def runwhile():
	k = 1
	global flag
	flag = True
	while flag:
		print(f'running thread \"{threading.current_thread().name}\"')
		k += 1
		time.sleep(1)

	print(f'While loop from thread \"{threading.current_thread().name}\" is over')

def runthread():
	thread = threading.Thread(target=runwhile)
	thread.start()

def printHello():
	print(f"Hello from \"{threading.current_thread().name}\"")


def stoploop():
	global flag
	flag = False
	print(f"changing flag from \"{threading.current_thread().name}\" ...")
	time.sleep(1.01)
	print(f"threads left: {list(thread.name for thread in threading.enumerate())}")
	

win =  tk.Tk()

ttk.Button(text='start', command=runthread).pack()
ttk.Button(text='stop', command=stoploop).pack()

ttk.Button(text='printHello', command=printHello).pack()
ttk.Button(text='quit', command=win.destroy).pack()



print(f"threads: {threading.enumerate()}")
win.mainloop()


# CLICKED BUTTONS:
# start 2 times
# printHello 2 times
# stop 1 time
# start 1 time
# printHello 1 times
# stop

# CONSOLE OUTPUT
# threads: [<_MainThread(MainThread, started 11108)>]
# running thread "Thread-1"
# running thread "Thread-2"
# running thread "Thread-1"
# running thread "Thread-2"
# Hello from "MainThread"
# Hello from "MainThread"
# running thread "Thread-1"
# running thread "Thread-2"
# changing flag from "MainThread" ...
# While loop from thread "Thread-1" is over
# While loop from thread "Thread-2" is over
# threads left: ['MainThread']
# running thread "Thread-3"
# running thread "Thread-3"
# Hello from "MainThread"
# running thread "Thread-3"
# running thread "Thread-3"
# changing flag from "MainThread" ...
# While loop from thread "Thread-3" is over
# threads left: ['MainThread']
