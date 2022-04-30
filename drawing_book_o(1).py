#https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
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
    # Write your code here
    # turns fro front 2t + 1 <= p
    # t <= (p - 1) / 2 # ceil
    # n - 2t <= p # if n is odd -> n = n - 1
    # t = (n - p) / 2 # ceil
    ft = math.ceil((p - 1) / 2)
    if n % 2 != 0:
        n = n - 1
    bt = math.ceil((n - p) / 2)
    return ft if ft < bt else bt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
