# Silver 5 - 카약과 강풍

import sys
input = sys.stdin.readline

def check(a):
    cnt = 0
    for k, v in a.items():
        if v == 0:
            cnt += 1
    return cnt

n, s, r = map(int, input().split())
d = {i:1 for i in range(1, n+1)}

for i in map(int, input().split()):
    d[i] -= 1
for i in map(int, input().split()):
    d[i] += 1

a = d.copy()
b = d.copy()

for i in range(1, n):
    if a[i] == 2 and a[i+1] == 0:
        a[i] -= 1
        a[i+1] += 1

for i in range(n, 1, -1):
    if b[i] == 2 and b[i-1] == 0:
        b[i] -= 1
        b[i-1] += 1

print(min(check(a), check(b)))