#https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.


def flatlandSpaceStations(n, c):
    c = sorted(c)
    maxD = 0
    for i, item in enumerate(c):
        if i == 0:
            maxD = 2 * item
        else:
            tempD = item - c[i - 1] - 1
            maxD = max(maxD, tempD)

    #calculate the maxD city after last station
    maxD = max(maxD, 2 * (n-1-c[-1]))
    return maxD//2 + (1 if maxD % 2 != 0 else 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
