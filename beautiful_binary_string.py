#https://www.hackerrank.com/challenges/beautiful-binary-string/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#


def beautifulBinaryString(b):
    # Write your code here
    s = "010"
    res = 0
    i = 0
    while i < len(b) - 2:
        if b[i: i+3] == s:
            res += 1
            i += 2
        i += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
