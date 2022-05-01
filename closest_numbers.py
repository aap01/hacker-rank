#https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    # Write your code here
    m = dict()
    repeats = set()
    for i in arr:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
            repeats.add(i)
    items = []
    if not repeats:
        arr = sorted(arr)
        mn = arr[1] - arr[0]
        for i in range(2, len(arr) - 1):
            tmp = arr[i + 1] - arr[i]
            if tmp < mn:
                mn = tmp
                items.clear()
            if tmp == mn:
                items.append(arr[i])
                items.append(arr[i + 1])
        return items
    else:
        for item in list(repeats):
            items += [item] * ((2 * (m[item] - 2) + 1) + 2)
    return items


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
