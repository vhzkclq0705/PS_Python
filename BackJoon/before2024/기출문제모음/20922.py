# Silver 1 - 겹치는 건 싫어

from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split())) + [0]
d = defaultdict(int)
left, right = 0, 0
d[nums[left]] = 1
cnt, ans = 1, 1

while right < n - 1:
    right += 1
    cnt += 1
    d[nums[right]] += 1

    if d[nums[right]] > k:
        while nums[left] != nums[right]:
            d[nums[left]] -= 1
            left += 1
            cnt -= 1
        d[nums[left]] -= 1
        left += 1
        cnt -= 1

    if ans < cnt:
        ans = cnt

print(ans)