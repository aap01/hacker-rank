#https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#


def acmTeam(topic):
    # Write your code here
    if not topic:
        return [0, 0]
    bitCount = len(topic[0])
    teamCount = 0
    mxTopicCount = 0
    d = dict()
    for i, p1 in enumerate(topic):
        if i == len(topic) - 1:
            break
        for j in range(i + 1, len(topic)):
            a1 = int(p1, 2)
            a2 = int(topic[j], 2)
            t = a1 | a2
            topicCount = 0
            if t in d:
                topicCount = d[t]
            else:
                for k in range(0, bitCount):
                    if (t >> k) & 1:
                        topicCount += 1
                d[t] = topicCount
            if topicCount > mxTopicCount:
                mxTopicCount = topicCount
                teamCount = 1
            elif topicCount == mxTopicCount:
                teamCount += 1

    return [mxTopicCount, teamCount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
