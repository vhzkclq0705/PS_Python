# Silver 1 - 하노이 탑 이동 순서

import sys
input = sys.stdin.readline

def move(n, a, b, c):
    if n == 1:
        ans.append((a, c))
        return
    
    move(n - 1, a, c, b)
    ans.append((a, c))
    move(n - 1, b, a, c)

n = int(input())
ans = []
move(n, 1, 2, 3)

print(len(ans))
[print(a, b) for a, b in ans]