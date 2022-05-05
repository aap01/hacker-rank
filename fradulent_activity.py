#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    # Write your code here

    # notices = 0
    # brute force TLE

    # for i in range(0, len(expenditure) - d):
    #     s = sorted(expenditure[i: i + d])
    #     med = 0
    #     if d % 2 == 0:
    #         med = (s[d // 2] + s[d // 2 - 1]) / 2

    #     else:
    #         med = s[(d - 1) // 2]

    #     nxt = i + d
    #     if nxt < len(expenditure) and expenditure[nxt] >= (2 * med):
    #         notices += 1
    # return notices

    def noticeCount(med, nxt):
        if nxt >= (2 * med):
            return 1
        return 0

    # Insertion sort technique
    # TLE
    # def insert(s, key):
    #     s.append(key)
    #     j = len(s) - 1
    #     while j > 0 and s[j - 1] > key:
    #         s[j] = s[j - 1]
    #         j -= 1
    #     s[j] = key

    # m = dict()
    # w = 0
    # s = []
    # notices = 0
    # for i in range(0, len(expenditure)):
    #     if i >= d:
    #         notices += noticeCount(s, expenditure[i])
    #         s.remove(expenditure[w]) # probably O(N)
    #         w += 1
    #     insert(s, expenditure[i])
    # return notices

    #Counting sort
    def countsToMedian(counts, d):
        j = k = 0
        if d % 2 == 0:
            j = d // 2 + 1
            k = d // 2
        else:
            j = d // 2 + 1
            k = j

        w = 0
        kth = -1
        jth = -1
        for i in range(0, 201):
            if (kth == -1) and (w + counts[i] >= k):
                kth = i
            if (jth == -1) and (w + counts[i] >= j):
                jth = i
            w += counts[i]
        return jth if j == k else (jth + kth) / 2

    notices = 0
    w = 0
    counts = [0] * 201
    for i in range(0, len(expenditure)):
        if i >= d:
            med = countsToMedian(counts, d)
            print(med)
            notices += noticeCount(med, expenditure[i])
            counts[expenditure[w]] -= 1
            w += 1
        counts[expenditure[i]] += 1

    return notices


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
