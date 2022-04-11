#https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    # Write your code here
    lenS = len(s)
    lenT = len(t)
    if k - lenS - lenT >= 0:  # Performing this operation on an empty string results in an empty string
        return 'Yes'
    # find the substring starting at index i in s that does not match with t anymore
    i = 0
    while i < lenS and i < lenT and s[i] == t[i]:
        i += 1
    if i == 0:
        k = k - lenS - lenT
    else:
        k = k - len(s[i:]) - len(t[i:])
    if k >= 0 and k % 2 == 0:  # k ops must be performed
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
