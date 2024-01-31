# Silver 1 - RGB거리

import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3):
        costs[i][j] = min(costs[i - 1][j - 1], costs[i - 1][j - 2]) + costs[i][j]

print(min(costs[-1]))