#!/usr/bin/python3

def permutations(array):
	'''
	It's not mine algorithm, it's from Narayana Pandit, God bless him!
	It's return list off all permutaions for the given sequence.
	Time of execution must be O(n), but I'm use reversed() function may be it ruined everything? 
		I don't know.

	'''

	n = len(array)
	result =[]
	result.append(array[:])

	while True:
		
		check = False

		for i in range(n - 1, 0, -1):
			if array[i-1] < array[i]:
				i -= 1
				check = True
				break
			
		if check == False: break # перебрали все перестановки

		min2 = array[i+1] # начинаем со следующего за i

		for digit in array[i+2:]:
			if digit < min2 and digit > array[i]: min2 = digit

		j = array.index(min2) 

		array[i], array[j] = array[j], array[i]
		
		array[i+1:] = reversed(array[i+1:])

		# print(array)

		result.append(array[:])

	# print(result)

	return result



def main():

	if permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]:
		print("Tests OK!")
	else:
		print("Fail")

main()