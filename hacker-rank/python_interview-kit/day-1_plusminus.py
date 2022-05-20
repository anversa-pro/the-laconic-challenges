#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# arr = [-4, 3, -9, 0, 4, 1]


def plusMinus(arr):

    length = len(arr)

    positive = [num for num in arr if num >= 1]
    negative = [num for num in arr if num <= -1]
    zero = length - (len(positive) + len(negative))

    print(f'{len(positive)/length: .6f}')
    print(f'{len(negative)/length: .6f}')
    print(f'{zero/length: .6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
