#https://www.hackerrank.com/challenges/sum-vs-xor/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def sumXor(n):
    # Write your code here
    # O(n) TLE
    # res = 1
    # for i in range(1, n + 1):
    #     if n + i == n ^ i:
    #         res += 1
    # return res
    # let a = 101101 => zeroCount = 2
    #     b = 000000
    #     c = 000010
    #     d = 010000
    #     e = 010010
    # n + i = n ^ i = 2**zeroCount = 2**2
    zeroCount = 0
    if n == 0:
        return 1
    while(n != 1):
        if not(n & 1):
            zeroCount += 1
        n = n >> 1
    return 2 ** zeroCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
