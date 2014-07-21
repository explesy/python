#!/usr/bin/python3

import random
import string
import re
import time

def pb_fill():
	""" Fill our phone book.
		Format: <phone_number> \t <name> \n
	 """

	number_of_records = 10000

	file = open('p_book.dat', 'w') 

	for i in range(number_of_records):

		phone = random.randint(1000000, 9999999)
		name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(random.randint(4, 10)))

		# print(phone, name)

		line = "{}\t{}\n".format(phone, name)

		file.write(line)

	file.close()

def pb_check():
	""" Check uniqueness of all phone numbers. """

	with open('p_book.dat', 'r') as file:
		phone = [line[:7] for line in file.readlines()]

	# print(phone)

	if(len(phone) == len(set(phone))):
		return True
	else:
		return False

def pb_read():
	""" Read data from our phone book file in 
		a. Dictionary
		b. List of Tuples
		c. Sorted by phone list of tuples
		and finally return the last thing.
	"""

	###DICTIONARY####################################################
	p_dict = {}
	with open('p_book.dat', 'r') as file:
		for line in file.readlines():
			phone = line[:7]
			name = re.sub('\d|\s', '', line)
			p_dict[phone] = name
			# print(p_dict)

	###LIST#OF#TUPLES################################################
	p_lotuple = []
	with open('p_book.dat', 'r') as file:
		for line in file.readlines():
			p_tuple = ()
			p_tuple += (line[:7], )
			p_tuple += (re.sub('\d|\s', '', line), )
			p_lotuple.append(p_tuple)
			del p_tuple
			# print(p_lotuple)

	###SORTED#LIST#OF#TUPLES#########################################
	p_lotuple_sorted = sorted(p_lotuple, key = lambda x : x[0])

	# print("\n\n\n")
	# print(p_lotuple_sorted)

	return p_lotuple_sorted

def pb_get_name(phone):
	""" Search in our phone book and return a name by phone. """
	pb = pb_read()
	for line in pb:
		if(int(line[0]) == phone):
			return line[1]
	return False


def pb_get_name_bi_way(phone):
	""" Search and return a name in our phone book by phone number.
		This function use kinda different algotithm compared with the previous.
		For algotithm thanks Niklaus Wirth and Internet.
		By the way it's almost usual bisection of our segment (list). """
	pb = pb_read()
	bottom = 0
	head = len(pb) - 1 
	while bottom < head:
		middle = int((bottom + head)/2)
		# print(pb[bottom][0], pb[middle][0], pb[head][0], phone)
		if(phone > int(pb[middle][0])):
			bottom = middle + 1  # we have plus one because one line above we use straight greater
		else:
			head = middle		# and here we can't use minus one, because not greater means lesser or *equal*

	if(int(pb[head][0]) == phone):
		return pb[head][1]
	else:
		return False

def pb_get_name_comparison(f, g, number):
	""" Here we will know who's faster and who have better performance.
		pb_get_name() vs pb_get_name_bi_way() """

	n = 10000
	counter = 0 
	time_sum_one = 0
	time_sum_two = 0

	while(counter < n):
		start = time.clock()
		f(number)
		time_sum_one += time.clock() - start

		start = time.clock()
		g(number)
		time_sum_two += time.clock() - start

		counter += 1

	print(time_sum_one, time_sum_two)

	if(time_sum_one < time_sum_two):
		print("First function faster in {} times".format(time_sum_one / time_sum_two))
	else:
		print("Second function faster in {} times".format(time_sum_two / time_sum_one))


def create():
	""" Create file with phone book were all phone numbers are uniq. """

	count = 0
	uniq = False

	while(not uniq):
		pb_fill()
		uniq = pb_check()
		count += 1
		print(count)

	print("Ready. Number of attempts: {}".format(count))

def test():
	""" Some tests for functions above.
		Uncomment to use. """
	# pb_read()

	number = 2590116

	# name = pb_get_name(number)
	# if(name): print("Phone: {}  -->  Name: {}".format(number, name))
	# else: print("We don't know this number!")

	# name = pb_get_name_bi_way(number)
	# if(name): print("Phone: {}  -->  Name: {}".format(number, name))
	# else: print("We don't know this number!")

	for _ in range(3):
		number_for_test = random.randint(1000000, 9999999)
		pb_get_name_comparison(pb_get_name, pb_get_name_bi_way, number_for_test)


create()
test()