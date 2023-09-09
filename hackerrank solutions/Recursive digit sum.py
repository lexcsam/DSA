#https://www.hackerrank.com/challenges/recursive-digit-sum/problem


import math
import os
import random
import re
import sys
def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    digit_sum = sum(int(digit) for digit in n)
    digit_sum *= k
    return superDigit(str(digit_sum), 1)
first_multiple_input = input().rstrip().split()
n = first_multiple_input[0]
k = int(first_multiple_input[1])
result = superDigit(n, k)
print(result)
