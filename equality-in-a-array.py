#https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def equalizeArray(arr):
    # Write your code here
    freq = dict()
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] = freq[i] + 1
    mx = max(freq[i] for i in freq)
    return len(arr) - mx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
