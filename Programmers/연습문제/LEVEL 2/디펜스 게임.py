# LEVEL 2

from heapq import heappush, heappop

def solution(n, k, enemy):
    hq = []

    for idx, e in enumerate(enemy):
        heappush(hq, -e)
        n -= e

        if n < 0:
            if k > 0:
                n -= heappop(hq)
                k -= 1
            else:
                return idx

    return len(enemy)
