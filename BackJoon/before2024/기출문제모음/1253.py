# Gold 4 - 좋다

import sys
input = sys.stdin.readline

def tp(tmp, i):
    global cnt
    start, end = 0, len(tmp) - 1

    while start < end:
        res = tmp[start] + tmp[end]
        if i == res:
            cnt += 1
            return
        elif i < res:
            end -= 1
        elif i > res:
            start += 1

n = int(input())
s = sorted(list(map(int, input().split())))
cnt = 0

for i in range(n):
    tp(s[:i] + s[i + 1:], s[i])

print(cnt)