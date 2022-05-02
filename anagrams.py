#https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def anagram(s):
    # Write your code here
    lenS = len(s)
    if lenS % 2 != 0:
        return -1
    mid = lenS//2
    s1 = s[0: mid]
    s2 = s[mid:]
    m = dict()
    count = 0
    for i in s1:
        if i not in m:
            m[i] = 0
        m[i] += 1
        count += 1
    for i in s2:
        if i in m:
            count -= 1
            m[i] -= 1
            if m[i] == 0:
                m.pop(i, None)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
