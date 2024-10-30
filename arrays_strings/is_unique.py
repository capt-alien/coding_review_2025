#!/opt/homebrew/bin/python3

"""
Impliment an algorythem to see if a string has all unique charictors. 

"""
def is_unique(string):
	chars = list(string)
	end = len(chars)
	for x in range(len(chars)):
		# print(chars[x+1:end])
		if chars[x] in chars[x+1:end]:
			return False
	return True


if __name__ == '__main__':
	string_1 = 'asdf'
	string_2 = 'abba'
	string_3 = 'eric bochcher'
	string_4 = 'abcdefg'

	print(is_unique(string_1))
	print(is_unique(string_2))
	print(is_unique(string_3))
	print(is_unique(string_4))