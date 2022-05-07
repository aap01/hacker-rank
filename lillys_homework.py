#https://www.hackerrank.com/challenges/lilys-homework/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
#https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def lilysHomework(arr):
    # Write your code here
    count = 0
    rCount = 0
    s = sorted(arr)
    idxMap = dict()
    arr2 = [i for i in arr]

    for i in range(0, len(arr)):
        idxMap[arr[i]] = i
    for i in range(len(arr)):
        if arr[i] != s[i]:
            count += 1
            idx = idxMap[s[i]]
            idxMap[arr[i]] = idx
            arr[idx], arr[i] = arr[i], s[i]

    for i in range(0, len(arr2)):
        idxMap[arr2[i]] = i
    s = list(reversed(s))
    for i in range(len(arr)):
        if arr2[i] != s[i]:
            rCount += 1
            idx = idxMap[s[i]]
            idxMap[arr2[i]] = idx
            arr2[idx], arr2[i] = arr2[i], s[i]

    mn = min(count, rCount)
    return mn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
