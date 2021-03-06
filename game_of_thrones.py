#https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def gameOfThrones(s):
    # Write your code here
    oddCount = 0
    m = dict()
    for i in s:
        if i not in m:
            m[i] = 0
        m[i] += 1
        if m[i] % 2 == 0:
            oddCount -= 1
        else:
            oddCount += 1
    if oddCount > 1:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
