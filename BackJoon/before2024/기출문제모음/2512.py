# Silver 3 - 예산

import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
m = int(input())

if sum(s) <= m:
    print(max(s))
else:
    start, end = 0, max(s)
    while start <= end:
        mid = (start + end) // 2
        tmp = list(map(lambda x: x if x <= mid else mid, s))
        
        if sum(tmp) <= m:
            start = mid + 1
        else:
            end = mid - 1
    
    print(start - 1)