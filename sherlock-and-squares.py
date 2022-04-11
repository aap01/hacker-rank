#https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#


def squares(a, b):
    # Write your code here
    l = int(math.sqrt(a))
    u = int(math.sqrt(b))
    res = 0
    for i in range(l, u + 1):
        s = i ** 2
        if s >= a and s <= b:
            res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
