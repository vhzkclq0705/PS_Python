# Silver 4 - 요세푸스 문제 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(range(1, n + 1))
idx = 0
ans = []

for i in range(n):
    idx += k - 1
    if idx >= (n - i):
        idx %= (n - i)
    ans.append(str(s.pop(idx)))

print('<', ', '.join(ans), '>', sep='')