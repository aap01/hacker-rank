#https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n):
    # Write your code here
    def add(p, q, c, bit):
        if len(q) > len(p):
            return add(q, p, c, bit)
        if len(p) >= bit:
            lenQ = len(q)
            cN, s = add(p[: -lenQ], q, c, bit)

            if cN != "0":
                return "0", cN + s
            return "0", s
        if c == "0":
            s = str(int(p) + int(q))
            print(s)
            if len(s) > len(q):
                return s[0], s[1:]
            return "0", s
        return add(p, str(int(q) + int(c)), "0", bit)

    def mul(p, q, bit):
        if len(q) > len(p):
            return mul(q, p, bit)
        if len(p) + len(q) >= bit:
            lenP = len(p)
            x = mul(p[: lenP//2], q, bit) + "0" * (lenP//2 + 1)
            y = mul(p[lenP // 2:], q, bit)
            return add(x, y, bit)
        x = int(p)
        y = int(q)
        return str(x * y)
    return add('10', '1', '1', 2)


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
