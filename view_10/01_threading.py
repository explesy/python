#!/usr/bin/python3

from threading import Thread, Lock

def f():
    global lock 
    with lock:
        while True:
            print(0)

def g():
    global lock 
    with lock:
        while True:
            print(1)

lock = Lock()
t1 = Thread(target=f)
t2 = Thread(target=g)
t1.start()
t2.start()
