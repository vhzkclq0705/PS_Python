# Silver 3 - 소수구하기

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
s = [True] * (n + 1)
s[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if s[i]:
        for j in range(2 * i, n + 1, i):
            s[j] = False

for i in range(m, n + 1):
    if s[i]:
        print(i)