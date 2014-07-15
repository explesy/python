#!/usr/bin/python3

#This function return integer in [a, b] range

def input_int(a, b):
	print("Please enter the number in [{}, {}] range".format(a,b))
	while True:
		print(">", end=' ')
		x = input()
		if x.isdigit():
			if(int(x) >= a and int(x) <= b):
				return x
			else:
				print("Only in [{}, {}] range. Try more.".format(a,b))
		else:
			print("Only numbers. Try more.")	
  

x = 1
y = 100

number = input_int(x, y)

print("Number from our function: {}".format(number))