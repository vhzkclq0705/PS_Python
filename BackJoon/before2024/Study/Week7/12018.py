# Silver 3 - Yonsei TOTO

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []
total, cnt = 0, 0

for _ in range(n):
    p, l = map(int, input().split())
    s = sorted(list(map(int, input().split())))

    if p < l:
        heappush(res, 1)
        continue
    
    for _ in range(l - 1):
        if len(s) > 1:
            s.pop()
    heappush(res, s[-1])

while res:
    n = heappop(res)
    if total + n <= m:
        total += n
        cnt += 1

print(cnt)