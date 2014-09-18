#!/usr/bin/python3

def longest_run(array):

	array.sort()

	result = []

	result.append(array[0])

	for i in range(1, len(array)):
		if array[i] != array[i-1] and array[i] - array[i-1] == 1:
			result.append(array[i])
	
	return result


def main():

	if longest_run([3, 6, 2, 4, 6, 2, 34, 4, 5]) == [2, 3, 4, 5, 6]:
		print("Tests OK!")
	else:
		print("Fail")

main()
