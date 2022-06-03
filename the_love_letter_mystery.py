#https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def theLoveLetterMystery(s):
    # Write your code here
    ops = 0
    lenS = len(s)
    for i in range(lenS // 2):
        ops += abs(ord(s[i]) - ord(s[lenS - i - 1]))
    return ops


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
