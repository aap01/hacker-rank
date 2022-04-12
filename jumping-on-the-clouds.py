#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    # Write your code here
    if len(c) == 1:
        return 0
    if 2 < len(c):
        if c[2] != 1:
            return 1 + jumpingOnClouds(c[2:])
    return 1 + jumpingOnClouds(c[1:])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
