# Gold 5 - 컨베이어 벨트 위의 로봇

from collections import deque
import sys
input = sys.stdin.readline

def down():
    b[n - 1] = False

def check(num):
    global k
    if a[num] == 0:
        k -= 1

n, k = map(int, input().split())
a = deque(map(int, input().split()))
b = deque([False] * n)
cnt = 0

while k > 0:
    cnt += 1

    a.rotate(1)
    b.rotate(1)
    down()

    for i in range(n - 2, -1, -1):
        if b[i] and not b[i + 1] and a[i + 1] > 0:
            a[i + 1] -= 1
            check(i + 1)
            b[i + 1] = True
            b[i] = False
    
    down()
    if a[0] > 0:
        a[0] -= 1
        check(0)
        b[0] = True

print(cnt)