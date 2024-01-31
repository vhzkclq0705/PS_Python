# Silver 1 - 행렬

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
b = [list(map(int, input().rstrip())) for _ in range(n)]
ans = 0

def flip(x, y):
    for i in range(3):
        for j in range(3):
            a[x+i][y+j] = 1 - a[x+i][y+j]

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            ans += 1
            flip(i, j)

print(ans if a == b else -1)