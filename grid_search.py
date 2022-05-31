#https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#


def gridSearch(G, P):
    # Write your code here
    # m = 0
    # for i in range(len(G)):
    #     for j in range(len(G[0])):
    #         if m == len(P) * len(P[0]):
    #             return 'YES'
    #         else:
    #             m = 0
    #         for k in range(len(P)):
    #             if i + k < len(G):
    #                 for l in range(len(P[0])):
    #                     if j + l < len(G[0]) and P[k][l] != G[i + k][j + l]:
    #                         break
    #                     else:
    #                         m += 1
    # return 'NO'
    # Brute Force TLE
    lenP = len(P)
    lenP0 = len(P[0])
    m = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if m == lenP:
                return 'YES'
            else:
                m = 0
                for k in range(len(P)):
                    if P[k] != G[i + k][j: j + lenP0]:
                        break
                    else:
                        m += 1
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
