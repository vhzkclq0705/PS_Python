# Silver 2 - 사람의 수

import sys
input = sys.stdin.readline

n = int(input())
s = {int(input().rstrip().split('.')[1]) for _ in range(n)}

for i in range(1, 1001):
    cnt = 0
    for j in range(i * 10 + 1):
        if j * 1000 // i in s:
            cnt += 1
    if cnt == n:
        print(i)
        break