# Silver 1 - 소수&팰린드롬

import sys
input = sys.stdin.readline

def isPrime(x):
    for i in range(2, int(n ** .5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
if n == 1:
    print(2)
else:
    while True:
        s = str(n)
        if s == s[::-1] and isPrime(n):
            print(n)
            break
        n += 1