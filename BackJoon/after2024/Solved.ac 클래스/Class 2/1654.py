# Silver 2 - 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]
start, end = 1, max(line)

while start <= end:
    half = (start + end) // 2
    cnt = 0

    for i in line:
        cnt += i // half
    
    if cnt < n:
        end = half - 1
    else:
        start = half + 1

print(end)