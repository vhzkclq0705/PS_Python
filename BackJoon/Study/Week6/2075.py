# Silver 2 - N번째큰 수

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    for num in list(map(int, input().split())):
        heappush(q, num)
        if len(q) > n:
            heappop(q)

print(heappop(q))