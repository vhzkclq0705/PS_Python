# Silver 4 - 요세푸스 문제

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(str, range(1, n + 1)))
ans = []
cnt = k - 1

for _ in range(n):
    ans.append(s.pop(cnt))
    if s:
        cnt = (cnt + k - 1) % len(s)

print('<' + ', '.join(ans) + '>')