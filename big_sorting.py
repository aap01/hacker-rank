#https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#


def bigSorting(unsorted):
    # Write your code here
    bucket = dict()
    index = 0
    sort = []
    while unsorted:
        for item in unsorted:
            idx = len(item) - 1 - index
            if idx >= 0:
                c = item[idx]
                val = int(c)
                if val not in bucket:
                    bucket[val] = []
                bucket[val].append(item)
        unsorted = []
        for k in range(0, 10):
            i = 0
            while k in bucket and i < len(bucket[k]):
                item = bucket[k][i]
                if len(item) > index + 1:
                    unsorted.append(bucket[k].pop(i))
                else:
                    sort.append(bucket[k].pop(i))
        index += 1
        # print(unsorted)
        # print(bucket, '\n')
    return sort


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
