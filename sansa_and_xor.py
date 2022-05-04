#https://www.hackerrank.com/challenges/sansa-and-xor/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def sansaXor(arr):
    # Write your code here
    # [1, 2, 3, 4]
    # 1, 2, 3, 4
    # (1, 2), (2, 3), (3, 4)
    # (1, 2, 3), (2, 3, 4)
    # (1, 2, 3, 4)

    # 1, 2, 3, 4, 5
    # (1, 2), (2, 3), (3, 4), (4, 5)
    # (1, 2, 3), (2, 3, 4), (3, 4, 5)
    # (1, 2, 3, 4), (2, 3, 4, 5)
    # (1, 2, 3, 4, 5)
    # Number of occurences of values at even index is odd

    lenA = len(arr)
    if lenA % 2 == 0:
        return 0
    i = 0
    res = 0
    while i < lenA:
        res ^= arr[i]
        i += 2
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
