# https://www.hackerrank.com/challenges/drawing-book/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    cf = 1
    cb = n if n % 2 == 0 else n - 1
    turn = 0
    while p > cf and p < cb:
        turn += 1
        cf += 2
        cb -= 2
    return turn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
