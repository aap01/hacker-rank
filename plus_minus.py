#https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1
    lenA = len(arr)
    pr = round(pos/lenA, 6)
    nr = round(neg/lenA, 6)
    zr = round(zero/lenA, 6)
    print(pr, nr, zr, sep='\n')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
