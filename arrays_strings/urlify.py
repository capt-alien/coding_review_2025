#!/opt/homebrew/bin/python3
"""
Write a mthod to replace all spaces in a string with '%20'
	- Assume that the space at the end of the string can hold aditional charictors
"""

def urlify(string):
	output_list = []
	new_string = 'www.'
	sub_char = '%20'
	string = string.strip()
	chars = list(string)
	for char in chars:
		if char == ' ':
			new_string = new_string + sub_char
		else:
			new_string = new_string + char
	return new_string+ '.com'


if __name__ == '__main__':
	string_1 = 'tom jones'
	string_2 = "testy Mc Testface  "
	string_3 = '    thats all there is    '

	print(urlify(string_1))
	print(urlify(string_2))
	print(urlify(string_3))
	