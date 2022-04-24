#https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    h = len(arr) - 1
    if h == 0:
        print(' '.join([str(i) for i in arr]))
    item = arr[h]
    while h - 1 >= 0 and item < arr[h - 1]:
        arr[h] = arr[h - 1]
        h -= 1
        print(' '.join([str(i) for i in arr]))
    arr[h] = item
    print(' '.join([str(i) for i in arr]))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
