#https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def funnyString(s):
    # Write your code here
    r = list(reversed(s))
    for i in range(0, len(s) - 1):
        if abs(ord(r[i]) - ord(r[i + 1])) != abs(ord(s[i]) - ord(s[i + 1])):
            return 'Not Funny'
    return 'Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
