#https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def makingAnagrams(s1, s2):
    # Write your code here
    m = dict()
    d = 0
    for i in s1:
        if i not in m:
            m[i] = 0
        m[i] += 1
        d += 1
    for i in s2:
        if i not in m:
            d += 1
        else:
            m[i] -= 1
            d -= 1
            if m[i] == 0:
                m.pop(i, None)
    return d


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
