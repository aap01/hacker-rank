#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, k):
    e = 100
    i = 0
    lenC = len(c)
    j = (i + k) % n
    if i == j:
        return e - (c[j]*2 + 1)
    e -= (c[j]*2 + 1)
    while j != 0:
        j = (j + k) % lenC
        e -= (c[j]*2 + 1)
        if e <= 0:
            return 0
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
