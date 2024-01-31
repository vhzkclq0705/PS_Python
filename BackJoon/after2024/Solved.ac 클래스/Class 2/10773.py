# Silver 4 - 제로

import sys
input = sys.stdin.readline

s = []

for i in range(int(input())):
    n = int(input())

    if n == 0:
        s.pop()
    else:
        s.append(n)

print(sum(s))