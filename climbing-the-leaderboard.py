#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # Write your code here
    m = []  # to store store ranked elements without repeats in it
    rankedLen = len(ranked)
    l = 0
    res = []

    while l < rankedLen:  # skipping repeats in ranked
        while l + 1 < rankedLen and ranked[l] == ranked[l + 1]:
            l += 1
        r = ranked[l]
        m.append(r)
        l += 1
    print(m)

    e = len(m) - 1
    s = 0

    while s < len(player):
        while e >= 0 and m[e] <= player[s]:
            e -= 1
        res.append(e + 2)
        s += 1
    return res


if __name__ == '__main__':
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
