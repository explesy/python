#!/usr/bin/python3

def is_correct2(string):

	if (string.count('(') == string.count(')') and \
	 string.count('[') == string.count(']') and \
	 string.count('{') == string.count('}')):
		return True
	else:
		return False

def is_correct(string):

	pns = 0
	bks = 0 
	bcs = 0

	for brkt in string:
		if(brkt == '('): pns += 1
		if(brkt == '['): bks += 1
		if(brkt == '{'): bcs += 1
		if(brkt == ')'): pns -= 1
		if(brkt == ']'): bks -= 1
		if(brkt == '}'): bcs -= 1

	print(pns, bks, bcs)

	if(pns == 0 and bks == 0 and bcs == 0):
		return True
	else:
		return False


def main():
	if	is_correct("[{}]()[()[]]") == True and \
		is_correct("[[}") == False and \
		is_correct("()(") == False and \
		is_correct(")[]") == False:
			print("Tests OK!")
	else:
		print("Fail")

main()