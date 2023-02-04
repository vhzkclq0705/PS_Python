# Gold 4 - 알파벳

import sys
input = sys.stdin.readline

# BFS
def bfs():
    global ans
    q = set([(0, 0, board[0][0])])

    while q:
        x, y, a = q.pop()
        ans = max(ans, len(a))

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in a:
                q.add((nx, ny, a + board[nx][ny]))

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = 0

bfs()
print(ans)

# Backtracking -> Python3 시간 초과, Pypy3 통과
# def dfs(x, y, cnt):
#     global ans
#     ans = max(ans, cnt)

#     for dx, dy in dxy:
#         nx, ny = x + dx, y + dy

#         if 0 <= nx < r and 0 <= ny < c and not visited[board[nx][ny]]:
#             visited[board[nx][ny]] = True
#             dfs(nx, ny, cnt + 1)
#             visited[board[nx][ny]] = False

# r, c = map(int, input().split())
# board = [list(map(lambda s: ord(s) - 65, input().rstrip())) for _ in range(r)]
# visited = [False] * 26
# visited[board[0][0]] = 1
# dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# ans = 0

# dfs(0, 0, 1)
# print(ans)