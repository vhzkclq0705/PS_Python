# Silver 2 - 골드바흐의 추측

import sys
input = sys.stdin.readline

def find_Primes(n):
    nums = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n ** .5) + 1):
        if nums[i]:
            for j in range(2 * i, n + 1, i):
                nums[j] = False

    return nums

s = [int(input()) for _ in range(int(input()))]
primes = find_Primes(max(s))
d = {i:[1, 10000] for i in s}

for i in s:
    for j in range(len(primes)):
        if primes[j] and primes[i - j]:
            d[i] = d[i] if abs(d[i][0] - d[i][1]) < abs(j - (i - j)) else [i - j, j]

for i in s:
    print(*d[i])