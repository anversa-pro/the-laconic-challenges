#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    if arr:
        min_sum = sum(arr)
        max_sum = 0
        for number in arr:
            total_sum = 0
            my_arr = list(arr)
            my_arr.pop(my_arr.index(number))
            for numb in my_arr:
                total_sum += numb
            if total_sum > max_sum:
                max_sum = total_sum
            if total_sum < min_sum:
                min_sum = total_sum

        print(f'{min_sum} {max_sum}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
