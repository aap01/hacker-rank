#https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(n, c):
    # Write your code here
    dp = [[0] * (n + 1)] * len(c)
    c = sorted(c)
    for i in range(len(c)):
        dp[i][0] = 1
        coin = c[i]
        for j in range(n + 1):
            if i == 0 and j % coin == 0:
                dp[i][j] = 1
            else:
                excluded = dp[i - 1][j]
                included = 0
                if j - coin >= 0:
                    included = dp[i][j - coin]
                dp[i][j] = excluded + included
    return dp[len(c) - 1][n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
