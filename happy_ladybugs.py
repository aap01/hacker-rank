#https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#


def happyLadybugs(b):
    # Write your code here
    # Initially it feels like
    # if there is at least one empty cell
    # and count of all colors is greater than 1
    # then all the ladybugs can be rearranged to stay happy
    # If there is an unhappy ladybug
    # then there must be at least one empty cell
    unhappy = False
    m = dict()
    e = 0
    for i, item in enumerate(b):
        if i > 0 and i < len(b) - 1 and item != "_" and not unhappy:
            unhappy = item != b[i - 1] and item != b[i + 1]
        if item == "_":
            e += 1
        elif item not in m:
            m[item] = 1
        else:
            m[item] += 1
    if not m:
        return 'YES'
    for item in m:
        if m[item] == 1:
            return 'NO'
    if e > 0 or not unhappy:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
