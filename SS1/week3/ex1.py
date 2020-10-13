#!/bin/python3

import math
import os
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for y in range(len(grades)):
        i = grades[y]
        if i > 37:
            if i % 5 == 3:
                i += 2
                grades[y] = i
            if i % 5 == 4:
                i += 1
                grades[y] = i

    return grades

if __name__ == '__main__':


    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
    print('\n')

