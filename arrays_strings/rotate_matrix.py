#!/opt/homebrew/bin/python3
import sys

"""
Problem: Rotate Matrix by 90 Degrees

You are given an  n \times n  matrix (a 2D list in Python) representing an image, where each element represents a pixel’s color in grayscale. Your task is to rotate the matrix 90 degrees clockwise in place.

Input:

	•	An  n \times n  list matrix of integers, where  1 \leq n \leq 20 .

Output:
	•	Modify the input matrix in place so that it is rotated 90 degrees clockwise.

Example:



"""

def rotate_one(m):
  return [[m[0][1], m[0][2], m[1][2]],
         [m[0][0], m[1][1], m[2][2]],
         [m[1][0], m[2][0], m[2][1]]
        ]

def roatate_n(matrix, n):
  new = matrix
  for x in range(n):
    new = rotate_one(new)

  return new

def ner(ele, n):
  return (ele + n) % 8


if __name__ == '__main__':
  matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
           ]
  n = int(sys.argv[1])
  # new= roatate_n(matrix,n)
  # for x in new:
  #   print(x)
  print(ner(1, n))







