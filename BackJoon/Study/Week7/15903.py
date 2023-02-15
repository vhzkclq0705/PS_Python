# Silver 1 - 카드 합체 놀이

from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
heapify(s)


for _ in range(m):
    a, b = heappop(s), heappop(s)
    heappush(s, a + b)
    heappush(s, a + b)

print(sum(s))
