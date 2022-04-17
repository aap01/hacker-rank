#https://www.hackerrank.com/challenges/maximizing-xor/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#


def maximizingXor(l, r):
    # Write your code here
    mx = 0
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            mx = max(mx, i ^ j)
    return mx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
