#!/usr/bin/python3

import time

#Recursive function for calculate Fibonacci sequence
#with some additional info
def fibo(n):
	global count
	print("Step " + str(count))
	print("Start count fibonachi number for " + str(n))
	print("n-2 \t n-1 \t n")
	print("{} \t {} \t {}".format(n-2, n-1, (n - 1 + n - 2)))

	count+=1

	if n == 0: return 0
	if n == 1: return 1
	return fibo(n - 1) + fibo(n - 2)

# Non recursive function for calculate Fibonacci sequence
def nacci(n):
	if (n == 0 or n == 1): return n
	p = 0
	k = 1
	result = 1
	count = 1
	while count < n:
		result = p + k
		p = k
		k = result
		count += 1
	return result  


def compare_functions(f, g, arg):
	i = 0
	t1 = 0
	t2 = 0
	while i < 1000:
		last_time = time.clock()
		f(arg)
		t1 += time.clock() - last_time
		last_time = time.clock()
		g(arg)
		t2 += time.clock() - last_time
		i += 1
	print("1st func time: {} \n2nd func time: {} \nFirst func faster\
			 in {} times".format(t1, t2, t1/t2))
	

#Global variable for counting inside recursive functions
count = 1 

# Compare time
compare_functions(fibo, nacci, 3)

# Another test for our functions
i = 5
n1 = fibo(i)
n2 = nacci(i)

if n1 == n2:
	print("They return same result!")
	print("Member of sequence: {} \n1st func result: {} \n2nd func result: {}".format(i, n1, n2))
else:
	print("Something go wrong. n1 != n2")
	print("Member of sequence: {} \n1st func result: {} \n2nd func result: {}".format(i, n1, n2))