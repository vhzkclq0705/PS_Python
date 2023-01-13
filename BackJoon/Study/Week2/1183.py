# Silver 3 - 약속

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
d = {}
max_Value = -(10e9)
min_Value = 10e9

for i in range(n):
    diff = s[i][1] - s[i][0]
    max_Value = max(max_Value, diff)
    min_Value = min(min_Value, diff)

for t in range(min_Value, max_Value + 1):
    sum_Value = 0
    for i in range(n):
        sum_Value += abs(s[i][0] + t - s[i][1])
    if sum_Value not in d:
        d[sum_Value] = 1
    else:
        d[sum_Value] += 1
print(d)
print(d[min(d)])