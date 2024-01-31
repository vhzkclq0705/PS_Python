# Silver 3 - 크리스마스 선물

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    a = list(map(int, input().split()))

    if a[0] == 0:
        print(heappop(hq) * -1 if hq else -1)
    else:
        for i in a[1:]:
            heappush(hq, -i)
