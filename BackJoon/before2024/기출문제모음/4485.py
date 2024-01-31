# Gold 4 - 녹색 옷 입은 애가 젤다지?

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def bfs():
    q = []
    heappush(q, (0, 0, 0))
    distance[0][0] = graph[0][0]

    while q:
        dis, x, y = heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] < dis:
                    continue
                total_dis = distance[x][y] + graph[nx][ny]
                if total_dis < distance[nx][ny]:
                    distance[nx][ny] = total_dis
                    heappush(q, (total_dis, nx, ny))

    return distance[-1][-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[sys.maxsize] * n for _ in range(n)]

    print(f'Problem {cnt}: {bfs()}')
    cnt += 1