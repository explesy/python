#!/usr/bin/python3

def find_nonpaired(digits):
	''' x, y, flag - 3 variables;
		for x ... & for y ... - 2 loops
		res[] - only to return answer from function, so if we rewrite it as one plain function
			we don't need it
  '''

	res = []

	for x in range(0, len(digits)):
		flag = False
		for y in range(0, len(digits)):
			if digits[x] == digits[y] and x != y:
				print(digits[x], digits[y])
				flag = True
		if not flag:
			res.append(digits[x])

	return res


def main():
	test = [2, 56, 23, 5, 7, 5, 7, 2]
	result = [56, 23]


	if find_nonpaired(test) == result:
		print("==> OK <==")
		print("{} nonpaired = {}".format(test, result))
	else:
		print("Something wrong")
		print("{} nonpaired != {}".format(test, result))
		

main()