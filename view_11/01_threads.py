#!/usr/bin/python3

from threading import Lock, Thread

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock4 = Lock()

# lock1.acquire()
lock2.acquire()

def f():
    print(0)
    lock1.acquire()
    print(1) 
    lock2.release()

def g():
    print(0)
    lock2.acquire()
    print(1)
    lock1.release()


t1 = Thread(target=f)
t2 = Thread(target=g)
t2.start()
t1.start()
