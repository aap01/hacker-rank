#https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


def timeInWords(h, m):
    # Write your code here
    d = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'quarter',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twnety four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eight',
        29: 'twenty nine',
        30: 'half'
    }
    if m == 0:
        return d[h] + ' ' + 'o\' clock'
    to = False
    if m > 30:
        m = 60 - m
        h = h + 1
        to = not to
    if m == 1:
        return f"{d[m]} minute {'to' if to else 'past'} {d[h]}"
    if m == 15 or m == 30:
        return f"{d[m]} {'to' if to else 'past'} {d[h]}"
    else:
        return f"{d[m]} minutes {'to' if to else 'past'} {d[h]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
