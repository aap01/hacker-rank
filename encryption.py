#https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    # Write your code here
    x = ""
    for i in s:
        if i != " ":
            x += i
    root = math.sqrt(len(x))
    r = math.floor(root)
    c = math.ceil(root)
    print(r, c)
    if r * c < len(x):
        r = c

    res = ""
    for j in range(c):
        for i in range(r):
            p = j + i * c
            if p < len(x):
                res += x[p]
        res += " "
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
