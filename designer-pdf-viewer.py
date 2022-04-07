#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#


def getIndex(c):
    return ord(c) - 97


def designerPdfViewer(h, word):
    # Write your code here
    word = word.strip()  # remove leading and trailing whitwspace
    length = len(word)
    if length == 0:
        return 0
    a = 0
    maxH = h[getIndex(word[0])]
    i = 1
    w = 1
    while i < length:
        if word[i] == ' ':  # care for space inside words
            a += w * maxH
            w = 0
            maxH = 0
        while word[i] == ' ' and i < length:  # skipping space inside words
            i += 1
        maxH = max(maxH, h[getIndex(word[i])])
        w += 1
        i += 1
    a += w * maxH
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
