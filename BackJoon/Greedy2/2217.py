# Silver 4 - 로프

import sys
input = sys.stdin.readline

ropes = sorted([int(input()) for _ in range(int(input()))], reverse=True)
ans = 0

while ropes:
    ans = max(ans, len(ropes) * ropes.pop())

print(ans)