# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#


def organizingContainers(container):
    # Write your code here
    # n balls of type t will take a container of capacity n to be isolated
    # if there are are enough containers for each type of balls then it is possible
    # as each swap exchanges two types of ball, a container of capacity n can be dropped with n number of same type balls
    # remainning containers can be dropped according to this logic
    caps = []
    types = []
    for i in container:
        caps.append(sum(i))
        for j, item in enumerate(i):
            if j >= len(types):
                types.append(0)
            types[j] += item
    caps = sorted(caps)
    types = sorted(types)
    for i, j in zip(caps, types):
        if i != j:
            return 'Impossible'
    return 'Possible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
