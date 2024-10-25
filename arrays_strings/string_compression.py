#!/opt/homebrew/bin/python3


"""
Write a function compress_string(s: str) -> str that takes a string s and compresses it using the following rules:

	1.	Consecutive repeating characters are replaced with the character followed by the count of its repetitions.
	2.	If a character appears only once, it should appear as-is without any count.

The function should return the compressed string only if it is shorter than the original string. If the compressed string is not shorter, return the original string instead.

Examples:

	compress_string("aaabbc")   # Output: "a3b2c"
compress_string("aabcccccaaa")  # Output: "a2b1c5a3"
compress_string("abc")      # Output: "abc" (since "a1b1c1" is longer than "abc")

""