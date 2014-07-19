#!/usr/bin/python3

import random
import string

def pb_fill():
	""" Fill our phone book
		Format: <phone_number> \t <name> \n
	 """

	number_of_records = 100000

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

def test():
	# pb_fill()
	# if(pb_check()): print("ok!")
	# else: print("not OK!") 

	count = 0
	uniq = False
	while(not uniq):
		pb_fill()
		uniq = pb_check()
		count += 1
		print(count)

	print("Final: {}".format(count))


test()