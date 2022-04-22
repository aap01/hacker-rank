#https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#


def stones(n, a, b):
    # Write your code here
    # Draw a tree for each stone
    # There is a common pattern in the tree
    # n-th stone can be of ia+(n-i-1)b for i can be 0 to n
    res = set()
    for i in range(0, n):
        inscription = a * i + (n - i - 1) * b
        res.add(inscription)
    res = list(res)
    return sorted(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
