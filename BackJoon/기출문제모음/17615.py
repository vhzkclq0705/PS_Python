# Silver 1 - 볼 모으기

import sys
input = sys.stdin.readline

def cnt(d, c):
    tmp = s.rstrip(c) if d else s.lstrip(c)
    ans.append(tmp.count(c))

n = int(input())
s = input().strip()
ans = []

cnt(True, 'R')
cnt(True, 'B')
cnt(False, 'R')
cnt(False, 'B')

print(min(ans))