#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s):
    # Write your code here
    i = 0
    h = 'hackerrank'
    for j in s:
        if j == h[i]:
            i += 1
        if i == len(h):
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
