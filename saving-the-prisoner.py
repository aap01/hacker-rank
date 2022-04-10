#https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#


def saveThePrisoner(n, m, s):
    # Write your code here
    # #ofBreads will be reduced to complete the first cycle numberOfReduced = (n - s) + 1
    # if numberOfReduced > m; Last bread will go to (s + m - 1)th person
    # Last of the remaining breads will go to the person
    # at index 1 + (m - numberOfReduced) % n
    # Above solution is not working
    # numR = n - s + 1
    # if numR >= m:
    #     return s + m - 1
    # else:
    #     return (m - numR) % n + 1

    #TLE for 6 cases
    # numR = n - s + 1
    # if numR >= m:
    #     return s + m - 1
    # else:
    #     return saveThePrisoner (n, m - numR, 1)

    # TLE solution
    # p = s
    # while m > 1:
    #     if p > n:
    #         p = 1
    #     p += 1
    #     m -= 1
    # return p

    return (m + s - 2) % n + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
