#https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def count(n, x):
    if n < x:
        return 0
    digitAtX = (n//x) % 10
    if digitAtX == 0:  # Number cannot be divided by zero
        return count(n, x*10)
    if n % digitAtX == 0:
        return 1 + count(n, x*10)
    return count(n, x*10)


def findDigits(n):
    # Write your code here
    # taking a map to store previous results
    return count(n, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
