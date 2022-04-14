#https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    x = sorted(a)
    res = 0
    i = 0
    while i < len(x):
        j = i + 1
        while j < len(x) and abs(x[j] - x[i]) <= 1:
            j += 1
        res = max(res, j - i)
        i += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
