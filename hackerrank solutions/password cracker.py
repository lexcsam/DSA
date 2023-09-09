#https://www.hackerrank.com/challenges/password-cracker/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def passwordCracker(passwords, loginAttempt):
    n = len(loginAttempt)
    dp = [None] * (n + 1)
    dp[0] = []
    for i in range(1, n + 1):
        for password in passwords:
            length = len(password)
            if i >= length and dp[i - length] is not None and loginAttempt[i - length:i] == password:
                if dp[i] is None or len(dp[i - length]) + 1 < len(dp[i]):
                    dp[i] = dp[i - length] + [password]
    if dp[n] is None:
        return "WRONG PASSWORD"
    else:
        return ' '.join(dp[n])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        fptr.write(result + '\n')

    fptr.close()
