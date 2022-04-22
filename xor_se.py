#https://www.hackerrank.com/challenges/xor-se/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.


def xorSequence(l, r):
    # In a=[0, 1, 3, 0, 4, 1, 7, 0, 8, 1, 11, 0, 12, 1, 15, 0...]
    # a[i * 4 - 1] = 0
    # indexOfZero = i * 4 - 1
    # indexOfZero = (l // 4) * 4 - 1 [i = l // 4]
    # So, a[indexOfZero + 1] = indexOfZero + 1

    # TLE
    # indexOfZero = (l // 4) * 4 - 1
    # if indexOfZero < 0:
    #     indexOfZero = 0
    # print(indexOfZero)
    # al = 0
    # for i in range(indexOfZero + 1, l + 1):
    #     al = al ^ i
    # a = [al]
    # k = 0
    # for i in range(l + 1, r + 1):
    #     a.append(a[k] ^ i)
    #     k += 1
    # res = 0
    # for i in a:
    #     res ^= i
    # return res

    # as Ax = Ax-1 ^ x
    # Al ^ Al+1
    # = Al ^ (Al ^ l+2)
    # = l+2

    # Al ^ Al+1 ^ Al+2
    # = Al ^ Al+1 ^ (Al+1 ^ l+2)
    # = Al ^ l+2

    # Al ^ Al+1 ^ Al+2 ^ Al+3 = Al ^ Al+1 ^ Al+2 ^ ((Al+2)^l+3)
    # = Al ^ Al+1 ^ (l+3) = Al ^ (Al ^ l+1) ^ L+3
    # = (l+1) ^ (l+3)

    # Al ^ Al+1 ^ Al+2 ^ Al+3 ^ Al+4
    # = Al ^ Al+1 ^ Al+2 ^ Al+3 ^ ((Al+3)^l+4)
    # = Al ^ Al+1 ^ Al+2 ^ (l+4)
    # = Al ^ Al+1 ^ (Al+1 ^ l+2) ^ l+4
    # = Al ^ l+2 ^ l+4

    # So if there are even number of terms in l->r
    # res = l+1 ^ l+3 ^ .. r
    # else
    # res = Al ^ l+2 ^ l+4

    # TLE
    # indexOfZero = (l // 4) * 4 - 1
    # if indexOfZero < 0:
    #     indexOfZero = 0
    # al = 0
    # res = 0
    # if (r - l + 1) % 2 == 0:
    #     k = l + 1
    #     while k <= r:
    #         res ^= k
    #         k += 2
    # else:
    #     for i in range(indexOfZero + 1, l + 1):
    #         al = al ^ i
    #     res = al
    #     k = l + 2
    #     while k <= r:
    #         res ^= k
    #         k += 2
    # return res

    #O(1)
    def elementAt(i):
        indexOfZero = (i // 4) * 4 - 1
        if indexOfZero < 0:
            indexOfZero = 0
        ai = 0
        for j in range(indexOfZero + 1, i + 1):
            ai = ai ^ j
        return ai
    # XOR-SUM of 8 elements is 0

    def xorSum(startI, endI):
        ei = elementAt(startI)
        si = ei
        for i in range(startI + 1, endI + 1):
            ei ^= i
            si ^= ei
        return si
    # find xorSum of elements starting from l to k-1
    # where k is the start of next group of 8s which xorSum to 0
    k = 8 + (l // 8) * 8
    if k >= r:
        return xorSum(l, r)

    sl = xorSum(l, k - 1)
    # find xorSum of elements starting from k to r
    # where k - 1 is the end of previous group of 8s which xorSum to 0
    k = (r // 8) * 8
    sr = xorSum(k, r)
    return (sl ^ sr) if k > l else sr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
