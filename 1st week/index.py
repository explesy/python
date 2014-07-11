#!/usr/bin/python3

import random

#random.seed()

i = 1

x = random.randint(1, 100)

s = 0

print(x)

print("Hello, my friend!")
print("Try to guess a number [1..100]")

while(s != x):
	i += 1
	s = int(input())	
	if(s > x):
		print("Try smaller")
		continue
	else:
		print("Try bigger")
	

print ("YEEEEEEEEEEES!")
#print ("You guessing in " + str(i) + " attempts")
#print("{}{}{}".format("You guessing in ", i, " attempts"))

print("You guessed in {} attempts".format(i))