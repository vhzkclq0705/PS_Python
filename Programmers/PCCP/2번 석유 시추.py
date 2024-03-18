# LEVEL 2 / 2번 / 석유 시추

from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    oil = []
    ans = [0] * m

    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        cnt = 1
        oil_y = {y}

        while q:
            x, y = q.popleft()
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
                    oil_y.add(ny)

        return (oil_y, cnt)

    for x in range(n):
        for y in range(m):
            if land[x][y] and not visited[x][y]:
                oil.append(bfs(x, y))

    for o, cnt in oil:
        for y in o:
            ans[y] += cnt

    return max(ans)