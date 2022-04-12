#https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def res(arr, r):
    l = len(arr)
    if l == 0:
        return r
    mn = min(arr)
    arr = [(i - mn) for i in arr if i - mn > 0]
    r.append(l)
    return res(arr, r)


def cutTheSticks(arr):
    # Write your code here
    return res(arr, [])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
