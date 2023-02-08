# Silver 2 - 최대 힙

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

h = []
for _ in range(int(input())):
    n = int(input())

    if n == 0:
        print(-heappop(h) if h else 0)
    else:
        heappush(h, -n)