# https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#


def workbook(n, k, arr):
    # Write your code here
    #  Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located\
    page = 0
    specials = 0
    for item in arr:
        page += 1
        for i in range(1, item + 1):
            if i == page:
                specials += 1
            if i % k == 0 and i != item:  # Don't add next blank page if no more problem left
                page += 1
    return specials


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
