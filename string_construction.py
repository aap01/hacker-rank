#https://www.hackerrank.com/challenges/string-construction/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def stringConstruction(s):
    # Write your code here
    # cost will be equal to the number of distinct chars
    m = dict()
    cost = 0
    for i in s:
        if i not in m:
            m[i] = 0
            cost += 1
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
