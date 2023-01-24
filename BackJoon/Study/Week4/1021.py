# Silver 4 - 회전하는 큐

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = deque(range(1, n + 1))
s = deque(map(int, input().split()))
ans = 0

while True:
    if not s:
        print(ans)
        break
    
    if nums[0] == s[0]:
        nums.popleft()
        s.popleft()
    else:
        find = nums.index(s[0])
        if find <= len(nums) // 2:
            nums.rotate(-1)
        else:
            nums.rotate(1)
        ans += 1