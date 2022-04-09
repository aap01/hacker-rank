#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

# n = 1234

# x = n % 10 # x = 4
# n = n // 10 # n = 123

# x = (10 * x) + (n % 10)
# n = n // 10


def reverese(n, x):
    if n < 10:
        return x * 10 + n 
    x = 10 * x + (n % 10)
    return reverese(n//10, x)


def beautifulDays(i, j, k):
    # Write your code here
    p = 0
    for x in range(i, j + 1):
        diff = abs(x - reverese(x, 0))
        res = diff % k

        if res == 0:
            p += 1
    return p



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
