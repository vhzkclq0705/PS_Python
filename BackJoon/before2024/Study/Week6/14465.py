# Silver 2 - 소가 길을 건너간 이유 5

import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
s = [0] * (n + 1)
left, right = 0, k

for _ in range(b):
    s[int(input()) - 1] = 1

SUM = sum(s[left:right])
ans = SUM

while right < n + 1:
    ans = min(ans, SUM)
    SUM = SUM - s[left] + s[right]
    left += 1
    right += 1

print(ans)