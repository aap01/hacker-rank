#https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def binSearch(arr, item, l, h):
    if l > h or l < 0 or h >= len(arr):
       return False
    mid = (l + h) // 2
    if arr[mid] == item:
        return mid
    if item > arr[mid]:
        return binSearch(arr, item, mid + 1, h)
    return binSearch(arr, item, l, mid - 1)


def beautifulTriplets(d, arr):
    # Write your code here

    if len(arr) < 3:
        return 0
    res = 0
    # O(n)
    di = dict()
    for item in arr:
        if item not in di:
            di[item] = 0
        di[item] += 1
    for item in arr:
        if item + d in di and item + 2*d in di:
            res += 1
    return res
    # O(nlogn)
    # for item in arr:
    #     if binSearch(arr, item + d, 0, len(arr) - 1) and binSearch(arr, item + 2 * d, 0, len(arr) -1 ):
    #         res += 1
    # return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
