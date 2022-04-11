#https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#


def permutationEquation(p):
    # Write your code here
    # Store the the element-index in key, value pair for O(1) lookup
    m = dict()
    res = []
    for i, e in enumerate(p):
        m[e] = i
    for i in range(1, len(p) + 1):
        x = m[i] + 1  # adding 1 since m[i] is zero based index
        y = m[x] + 1
        res.append(y)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
