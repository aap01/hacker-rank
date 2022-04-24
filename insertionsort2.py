#https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort2(n, arr):
    # Write your code here
    def insert(arr, h):
        item = arr[h]
        while arr[h] < arr[h - 1] and h - 1 >= 0:
            arr[h] = arr[h - 1]
            arr[h - 1] = item
            h -= 1
        if h == 0:
            arr[h] = item
        print(' '.join(str(i) for i in arr))

    for i in range(1, len(arr)):
        insert(arr, i)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
