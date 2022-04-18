#https://www.hackerrank.com/challenges/counter-game/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def winner(n, s=0, names=['Louise', 'Richard']):
    if n == 1:
        return names[1 - s]
    x = int(math.log2(n))
    if 2**x == n:
        return winner(n//2, 1 - s, names)
    return winner(n - 2**x, 1 - s, names)


def counterGame(n):
    # Write your code here
    return winner(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
