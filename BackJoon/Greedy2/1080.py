# Silver 1 - 행렬

import sys
input = sys.stdin.readline

def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            first[i][j] = 1 - first[i][j]

n, m = map(int, input().split())
first = [list(map(int, input().rstrip())) for _ in range(n)]
second = [list(map(int, input().rstrip())) for _ in range(n)]
ans = 0

for i in range(n - 2):
    for j in range(m - 2):
        if first[i][j] != second[i][j]:
            reverse(i, j)
            ans += 1

print(ans if first == second else -1)