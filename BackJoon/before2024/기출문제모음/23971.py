# Bronze 3 - ZOAC 4

import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())
row, col = 0, 0

for _ in range(0, h, n + 1):
    row += 1
for _ in range(0, w, m + 1):
    col += 1

print(row * col)