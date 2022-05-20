#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    am_pm = s[-2::]
    time = s[:-2:].split(':')
    if am_pm.lower() == 'am':
        if time[0] == '12':
            return f'00:{time[1]}:{time[2]}'
        return s[:-2:]
    elif am_pm.lower() == 'pm':
        if time[0] == '12':
            return s[:-2:]
        return f'{int(time[0]) + 12}:{time[1]}:{time[2]}'
    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
