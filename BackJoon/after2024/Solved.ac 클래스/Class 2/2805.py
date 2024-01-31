# Silver 2 - 나무 자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
start, end = 0, max(s)
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in s:
        if i >= mid:
            cnt += i - mid
    
    if cnt < m:
        end = mid - 1
    else:
        start = mid + 1
        ans = max(ans, mid)

print(ans)