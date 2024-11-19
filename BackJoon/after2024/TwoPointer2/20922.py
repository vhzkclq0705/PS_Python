# BOJ
# S1 - 20922(겹치는 건 싫어)

import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = defaultdict(int)
l, r = 0, 0
ans = 0

while r < n:
    if cnt[nums[r]] < k:
        cnt[nums[r]] += 1
        r += 1
        ans = max(ans, r - l)
    else:
        cnt[nums[l]] -= 1
        l += 1
    
print(ans)