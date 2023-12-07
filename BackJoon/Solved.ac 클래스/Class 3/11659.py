# Silver 3 - 구간 합 구하기 4

import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
acc = [0] + list(accumulate(nums))

for _ in range(m):
    start, end = map(int, input().split())
    print(acc[end] - acc[start - 1])