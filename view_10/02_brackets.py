#!/usr/bin/python3

def is_correct(string):

	if (string.count('(') == string.count(')') and \
	 string.count('[') == string.count(']') and \
	 string.count('{') == string.count('}')):
		return True
	else:
		return False


def main():
	if	is_correct("[{}]()[()[]]") == True and \
		is_correct("[[}") == False and \
		is_correct("()(") == False:
			print("Tests OK!")
	else:
		print("Fail")

main()