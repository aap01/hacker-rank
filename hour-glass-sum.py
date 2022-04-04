#https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    w = 3  # max width of hourglass
    arrLen = len(arr)
    # min possible sum for an hourglass based on definition of inputset
    res = - (7 * 9)
    for i in range(arrLen - 2):
        for j in range(len(arr[0]) - 2):
            topRowSum = sum(arr[i][j: j + w])
            center = arr[i + 1][j + 1]
            bottomRowSum = sum(arr[i + 2][j: j + w])
            sm = topRowSum + center + bottomRowSum
            res = max(res, sm)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
