#https://www.hackerrank.com/challenges/tutorial-intro/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#


def introTutorial(V, arr):
    # Write your code here
    def binSearch(V, arr, l, h):
        if l >= h:
            return l
        m = (l + h)//2
        mid = arr[m]
        if mid == V:
            return m
        if mid > V:
            return binSearch(V, arr, l, m - 1)
        return binSearch(V, arr, m + 1, h)

    return binSearch(V, arr, 0, len(arr) - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
