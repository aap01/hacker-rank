#https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def minimumDistances(a):
    # Write your code here
    d = dict()
    mn = len(a)
    for i, item in enumerate(a):
        if item in d:
            mn = min(mn, i - d[item])
        d[item] = i
    return mn if mn != len(a) else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
