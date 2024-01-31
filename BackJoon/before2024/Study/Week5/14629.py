# Silver 1 - 숫자 조각

import sys
input = sys.stdin.readline

def bt(num, depth):
    global min_Value, ans

    if depth == l:
        if min_Value > abs(num - n):
            min_Value = abs(num - n)
            ans = num
        return
    
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            bt(num * 10 + i, depth + 1)
            visited[i] = False

n = int(input())
l = len(str(n))
visited = [False] * 10
min_Value = sys.maxsize
ans = 0

if n >= 9876543210:
    print(9876543210)
else:
    bt(0, 0)
    print(ans)