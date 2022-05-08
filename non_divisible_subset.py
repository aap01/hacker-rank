#https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    # Result can come from two subsets
    # data = {x: x = i%k; i belongs to s}
    # pick x and find the count of k - x in remainders set
    # subtract count from total remainders
    # find max of these results
    # Special case 0s; only one zero is acceptable in any of those subsets

    counts = dict()
    total = len(s)
    for i in s:
        mod = i % k
        if mod not in counts:
            counts[mod] = 0
        counts[mod] += 1
    count = 0
    i = 1
    while i < k - i:
        mx1, mx2 = 0, 0
        if i in counts:
            mx1 = counts[i]
        if (k - i) in counts:
            mx2 = counts[k-i]
        count += max(mx1, mx2)
        i += 1
    if i in counts and i == k - i:
        count += 1
    if 0 in counts:
        count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
