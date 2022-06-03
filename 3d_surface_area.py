#https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


def surfaceArea(A):
    # Write your code here
    top = len(A) * len(A[0])
    bottom = top
    sides = 0
    #Calculate only sided
    for i in range(len(A)):
        for j in range(len(A[0])):
            withPrevRow = [A[i][j], max(0, A[i][j] - A[i - 1][j])][i > 0]
            withNextRow = [lambda: A[i][j], lambda: max(
                0, A[i][j] - A[i + 1][j])][i < len(A) - 1]()  # Fancy ternary op :D
            withPrevColumn = max(
                0, A[i][j] - A[i][j - 1]) if j > 0 else A[i][j]
            withNextColumn = max(
                0, A[i][j] - A[i][j + 1]) if j < len(A[0]) - 1 else A[i][j]
            sides += withPrevRow + withNextRow + withPrevColumn + withNextColumn
    return top + bottom + sides


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
