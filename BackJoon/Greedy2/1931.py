# Silver 1 - 회의실 배정

import sys
input = sys.stdin.readline

meeting = [list(map(int, input().split())) for _ in range(int(input()))]
meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

ans = 0
time = 0
for start, end in meeting:
    if start >= time:
        time = end
        ans += 1

print(ans)