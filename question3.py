#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#
def twoStacks(maxSum, a, b):

    # Write your code here
    i = j = s = 0

    while i < len(a) and s + a[i] <= maxSum:
        s += a[i]
        i += 1 
    n = maxn = i
    i -= 1

    while j < len(b):
        if s + b[j] <= maxSum:
            s += b[j]
            j += 1
            n += 1
            maxn = max(maxn, n)

        elif i >= 0:
            s -= a[i]
            i -= 1
            n -= 1

        else:
            break

    return maxn
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
