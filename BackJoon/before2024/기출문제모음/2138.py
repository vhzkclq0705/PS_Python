# Gold 5 - 전구와 스위치

import sys
input = sys.stdin.readline

def turn(a, b):
    tmp = a[:]
    cnt = 0
    for i in range(1, n):
        if tmp[i - 1] == b[i - 1]:
            continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                tmp[j] = 1 - tmp[j]
    
    return cnt if tmp == b else sys.maxsize

n = int(input())
a = list(map(int, input().rstrip()))
b = list(map(int, input().rstrip()))

ans = turn(a, b)
a[0] = 1 - a[0]
a[1] = 1 - a[1]
ans = min(ans, turn(a, b) + 1)

print(-1 if ans == sys.maxsize else ans)