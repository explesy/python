#!/usr/bin/python3

from math import sqrt

def maximum_prime(n):
	if(is_prime(n)):
		return n
	m = int(round(sqrt(n)))
	result = []
	while(m >= 2):
		# print(result, m)
		if(n % m == 0):
			if(is_prime(m)):
				result.append(m)
			if(is_prime(int(n/m))):
				result.append(n/m)
		m -= 1

	return int(max(result))


# Shitty algothm for prime checking
def is_prime(number):
	for i in range(2, number):
		if (number % i == 0):
			return False

	return True


def test():
	#Big number test
	print (maximum_prime(4294967297))

	#Range test
	for i in range(1, 101):
		print (i, maximum_prime(i))


test()
