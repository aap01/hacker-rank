#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'superFunctionalStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def dis(x):
    d = dict()
    for i in x:
        d[i] = True
    return len(''.join(d.keys()))


def superFunctionalStrings(s):
    # Write your code here
    d = dict()
    sm = 0
    for i in range(1, len(s) + 1):
        for x in range(0, len(s)):
            ss = s[x: x + i]
            if ss not in d:
                d[ss] = True
                l = len(ss)
                di = dis(ss)
                print(f'distinct {ss} is {di}')
                sm += pow(l, di) % 10000007
    print(d)
    return sm


print(superFunctionalStrings('aa'))