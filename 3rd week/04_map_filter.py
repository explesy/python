#!/usr/bin/python3

def my_map(func, lst):
	""" I'm a cool guy and I have ma own map() function.
		I don't know for what, but who cares? """
	
	new_lst = [func(number) for number in lst]

	return new_lst

def my_filter(func, lst):
	""" Same shit """

	new_lst = [number for number in lst if(func(number))]

	return new_lst

def test_map(x):
	return x * x * x

def test_filter(x):
	if(2 < x < 7):
		return x
	else:
		return False

def test():

	lst = list(range(10))

	print(lst)

	if(my_map(test_map, lst) == list(map(test_map, lst))):
		print("map() and my_map() functions are equal.")
		print(list(map(test_map, lst)))
		print(my_map(test_map, lst))
	else: 
		print("map() and my_map() functions not equal.")
		print(list(map(test_map, lst)))
		print(my_map(test_map, lst))


	if(my_filter(test_filter, lst) == list(filter(test_filter, lst))):
		print("filter() and my_filter() functions are equal.")
		print(list(filter(test_filter, lst)))
		print(my_filter(test_filter, lst))
	else: 
		print("filter() and my_filter() functions not equal.")
		print(list(filter(test_filter, lst)))
		print(my_filter(test_filter, lst))

test()