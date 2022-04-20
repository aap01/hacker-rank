#https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    # TLE
    if s < p:
        return 0
    if p - d > m:
        return 1 + howManyGames(p - d, d, m, s - p)
    else:
        return 1 + (s-p)//m
    # |i(p - id) = m
    # n = (p - m) / d
    # n = floor((p - m) / d)
    # s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
