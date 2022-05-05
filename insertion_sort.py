#https://www.hackerrank.com/challenges/insertion-sort/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def inversionCount(arr):
    if len(arr) > 1:
        leftArr = arr[: len(arr) // 2]
        rightArr = arr[len(arr) // 2:]
        icL = inversionCount(leftArr)
        icR = inversionCount(rightArr)
        ic = 0
        i = 0
        j = 0
        h = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] > rightArr[j]:
                ic += (len(leftArr) - i)
                arr[h] = rightArr[j]
                j += 1
            else:
                arr[h] = leftArr[i]
                i += 1
            h += 1
        while i < len(leftArr):
            arr[h] = leftArr[i]
            i += 1
            h += 1
        while j < len(rightArr):
            arr[h] = rightArr[j]
            j += 1
            h += 1
        return ic + icL + icR
    return 0


def insertionSort(arr):
    # Write your code here
    # Inversion count is the way to tell how many shifts are needed
    # 3 Methods to count inversions
    # 1. Brute Force
    # 2. Merge sort algorithm
    # 3. Fenwick Tree/ Binary Indexed Tree

    # 2. Using merge sort
    # Terminated due to timeout :(
    # return inversionCount(arr)

    # 3. Fenwick Tree/ Binary Indexed Tree
    def add(bTree, idx, val):
        while idx < len(bTree):
            bTree[idx] += val
            idx += idx & -idx

    def getSum(bTree, r):
        s = 0
        while r > 0:
            s += bTree[r]
            r -= r & -r
        return s

    m = dict()
    lenA = len(arr)
    arr2 = [0] * lenA
    for i in arr:
        if i not in m:
            m[i] = 0
    newVal = 1
    for i in sorted(m.keys()):  # sorting on keys ascending
        m[i] = newVal
        newVal += 1
    i = 0
    for j in arr:
        arr2[i] = m[j]
        i += 1

    bTree = [0] * (newVal)  # initiating a Binary Indexed Tree
    ic = 0
    for i in list(reversed(arr2)):  # reversing the list
        ic += getSum(bTree, i - 1)
        add(bTree, i, 1)
    print(bTree)
    return ic


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
