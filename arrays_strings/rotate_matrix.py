#!/opt/homebrew/bin/python3
import sys

"""
Problem: Rotate Matrix by 90 Degrees

given an image represented by an N*N matrix, where each pixle is represented
by an integer, write a method to rotate the image 90 degrees. 


"""

# def rotate_one(m):
#   return [[m[0][1], m[0][2], m[1][2]],
#          [m[0][0], m[1][1], m[2][2]],
#          [m[1][0], m[2][0], m[2][1]]
#         ]

# def roatate_n(matrix, n):
#   new = matrix
#   for x in range(n):
#     new = rotate_one(new)

#   return new

#this should be a simple transpose problem. 


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







