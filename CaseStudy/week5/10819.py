import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
per = permutations(s)
ans = []

for p in per:
    total = 0
    for i in range(n - 1):
        total += abs(p[i] - p[i + 1])
    ans.append(total)

print(max(ans))