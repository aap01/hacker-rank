#https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#


def gemstones(arr):
    # Write your code here
    lenA = len(arr)
    if lenA == 1:
        return len(arr[0])

    m = dict()
    for item in arr:
        temp = dict()
        for c in item:
            if c not in m:
                m[c] = 0
            if c not in temp:
                temp[c] = True
                m[c] += 1
    gems = 0
    for i in m:
        if m[i] == lenA:
            gems += 1

    return gems


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
