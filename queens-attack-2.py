#https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def hasNoObstacle(grid, i, j):
    return not (i in grid and j in grid[i])


def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    u = 0
    ldu = 0
    l = 0
    ldb = 0
    b = 0
    rdb = 0
    r = 0
    rdu = 0

    # grid = [[0]*n]*n this cannot be used as its child list are same instance
    grid = dict()
    print(obstacles)
    for item in obstacles:
        row = item[0] - 1  # rotate the grid
        column = item[1] - 1  # rotate the grid
        if row not in grid:
            grid[row] = dict()
        grid[row][column] = 1
    print(grid)

    # bottom
    i = r_q - 1  # vertically inverting the grid
    j = c_q - 1
    while i - 1 >= 0 and hasNoObstacle(grid, i - 1, j):
        b += 1
        i -= 1

    # left diagonal bottom
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while i - 1 >= 0 and j - 1 >= 0 and hasNoObstacle(grid, i - 1, j - 1):
        ldb += 1
        i -= 1
        j -= 1

    # left
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while j - 1 >= 0 and hasNoObstacle(grid, i, j - 1):
        l += 1
        j -= 1

    # left diagonal up
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while i + 1 < n and j - 1 >= 0 and hasNoObstacle(grid, i + 1, j - 1):
        ldu += 1
        i += 1
        j -= 1

    # u
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while i + 1 < n and hasNoObstacle(grid, i + 1, j):
        u += 1
        i += 1

    # bottom right diagonal
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while i + 1 < n and j + 1 < n and hasNoObstacle(grid, i + 1, j + 1):
        rdu += 1
        i += 1
        j += 1

    # right
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while j + 1 < n and hasNoObstacle(grid, i, j + 1):
        r += 1
        j += 1

    # right diagonal bottom
    i = r_q - 1  # recentering the queen
    j = c_q - 1
    while i - 1 >= 0 and j + 1 < n and hasNoObstacle(grid, i - 1, j + 1):
        rdb += 1
        j += 1
        i -= 1
    return u + ldu + l + ldb + b + rdb + r + rdu


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
