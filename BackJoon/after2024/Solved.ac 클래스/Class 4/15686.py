# Gold 5 - 치킨 배달

# Combination
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# ans = 999999
# chickens = []
# houses = []

# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 1:
#             houses.append((i, j))
#         elif board[i][j] == 2:
#             chickens.append((i, j))

# for chicken in combinations(chickens, m):
#     dis = 0
#     for hx, hy in houses:
#         min_dis = 100
#         for i in range(m):
#             min_dis = min(min_dis, abs(hx - chicken[i][0]) + abs(hy - chicken[i][1]))
#         dis += min_dis

#     ans = min(ans, dis)

# print(ans)

# Back Tracking
import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global ans
    if depth == m:
        dis = 0
        for hx, hy in houses:
            min_dis = 100
            for cx, cy in q:
                min_dis = min(min_dis, abs(hx - cx) + abs(hy - cy))
            dis += min_dis
        ans = min(ans, dis)
        return
    
    for i in range(idx, len(chickens)):
        q.append(chickens[i])
        dfs(depth + 1, i + 1)
        q.pop()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 999999
q = []
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

dfs(0, 0)
print(ans)