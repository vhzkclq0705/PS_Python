# BOJ
# S3 - 21921(블로그)

import sys
from collections import defaultdict
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

if sum(visitors) == 0:
    print("SAD")
else:
    total = sum(visitors[:x])
    results = defaultdict(int)
    results[total] += 1

    for i in range(1, n - x + 1):
        total = total - visitors[i - 1] + visitors[i + x - 1]
        results[total] += 1

    max_visitors = max(results)

    print(max_visitors)
    print(results[max_visitors])