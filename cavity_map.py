#https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#


def cavityMap(grid):
    # Write your code here
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            item = int(grid[i][j])
            top = grid[i - 1][j]
            left = grid[i][j - 1]
            right = grid[i][j + 1]
            bottom = grid[i + 1][j]
            if left == "X" or right == "X" or top == "X" or bottom == "X":
                continue
            top = int(top)
            left = int(left)
            bottom = int(bottom)
            right = int(right)
            if item > top and item > left and item > bottom and item > right:
                grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
