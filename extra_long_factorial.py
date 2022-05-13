#https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n):
    res = [1]
    c = 0
    for i in range(2, n + 1):
        for j in range(0, len(res)):
            p = len(res) - j - 1
            tmp = i * res[p] + c
            res[p] = tmp % 10
            c = tmp // 10
        while c > 0:
            res = [c % 10] + res
            c = c // 10
    print(''.join([str(i) for i in res]))


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
