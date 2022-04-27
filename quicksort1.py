#https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quickSort(arr):
    # Write your code here
    def Sort(arr, l, h):
        if l >= h:
            return
        p = l
        for i in range(l + 1, h + 1):
            if arr[p] > arr[i]:
                arr[i], arr[p], arr[p + 1] = arr[p + 1], arr[i], arr[p]
                p += 1

        Sort(arr, l, p-1)
        Sort(arr, p + 1, h)
        return arr
    return Sort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
