#https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def countA(s, n):
    if not s or n == 0:
        return 0
    if s[0] == "a":
        return 1 + repeatedString(s[1:], n - 1)
    return repeatedString(s[1:], n - 1)


def repeatedString(s, n):
    # Write your code here
    lenS = len(s)
    if lenS < n:
       q = n//lenS
       r = n % lenS
       qc = countA(s, lenS)  # nubmerOf a's in its current length
       rc = countA(s, r)  # number of a's in its remainder length
       return q * qc + rc  # number of a's in its infinite length = n
    return countA(s, n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
