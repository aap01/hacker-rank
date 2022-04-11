#https://www.hackerrank.com/challenges/circular-array-rotation/
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#


def circularArrayRotation(a, k, queries):
    # Write your code here
    # let ic is the current index and its previous index was i0
    # if we rotate the array k times then the following eqn holds
    # ic = (i0 + k) % n .....(i)
    # i0 + k = ic mod n
    # i0 = (ic - k) mod n
    # if ic - k < 0:
    # i0 = (ic - k  + n) mod n
    res = []
    for i in queries:
        p = i - k
        if i - k < 0:
            p = n + i - k
        res.append(a[p % n])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
