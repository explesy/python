#!/usr/bin/python3

def sieve(bound):
	""" Sieve of Eratosthenes. Find all prime numbers up to bound. """
	numbers = list(range(2,bound+1))
	# print(numbers)
	p = 2
	while(p != numbers[-1]):
		for i in numbers:
			if(i%p == 0 and i != p): 
				numbers.remove(i)
				# print(numbers)
		p = numbers[numbers.index(p)+1]
	return numbers


def test():	
	""" Test function """
	test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	n = 100
	if(test == sieve(n)):
		print("OK")
	else:
		print("Wrong")
	print(sieve(n))

test()