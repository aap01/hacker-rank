#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def digits(n):
    if n < 10:
        return 1
    return 1 + digits(n//10)


def kaprekarNumbers(p, q):
    # Write your code here
    res = []
    for x in range(p, q + 1):
        sqr = x ** 2
        rem = digits(x)
        s1 = sqr // (10**rem)
        s2 = sqr - s1 * (10**rem)
        # print(rem)
        # print(sqr)
        # print(s1)
        # print(s2, '\n')
        if s1 + s2 == x:
            res.append(x)
    res = [str(i) for i in res]
    print(" ".join(res)) if res else print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
