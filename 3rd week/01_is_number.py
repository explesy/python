#!/usr/bin/python3

def is_number(number):
	""" Check is our input is a number """
	import re
	pattern = re.compile('^-?\d+\.?\d*$')
	match = pattern.match(number)
	if match:
		return True
	else:
		return False


def test():	
	""" Test for is_number functions """
	test = ["243", "-243", "0.5", "-0.5", "erjei253", "3543fie", "gejg353ji", "@$(^@)(*"]
	for i in test:
		if(is_number(i)):
			print("[V]", i)
		else:
			print("[ ]", i)
	# while True:
	# 	number = input("Please input something: ")
	# 	if(is_number(number)):
	# 		print("We have a number")
	# 	else:
	# 		print("It's don't looks like a number")

test()