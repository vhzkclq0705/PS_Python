# Silver 4 - 베스트셀러

import sys
input = sys.stdin.readline

d = {}
for _ in range(int(input())):
    s = input().rstrip()
    d[s] = d[s] + 1 if s in d else 1
r = sorted([k for k, v in d.items() if max(d.values()) == v])
print(r[0])