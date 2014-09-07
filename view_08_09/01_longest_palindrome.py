#!/usr/bin/python3

def longest_palindrome(poly):
	''' Return longest polindrome in given string '''

	n = 2
	substrings = []
	max_poly = ""
	length = 0

	for x in range(0, len(poly) - 1):
		for y in range(n, len(poly) + 1):
			substrings.append(poly[x:y])
		n += 1

	for x in substrings:
		if x == x[::-1] and len(x) > length:
			max_poly = x
			length = len(x)

	return max_poly


def main():
	
	test = [
			["xxabcbaay", "abcba"],
			["xax", "xax"],
			["xaax", "xaax"],
			["ddkgenrpkttyttkpehtngnknan", "pkttyttkp"]
		   ]

	for x, y in test:
		if longest_palindrome(x) == y:
			print("[OK] longest palindrome of {} == {}".format(x, y))
		else:
			print("[XX] longest palindrome of {} == {}".format(x, y))


main()