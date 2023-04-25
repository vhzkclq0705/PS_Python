# LEVEL 2

def solution(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    ans = []
    
    for x in range(n):
        for y in range(m):
            for d in range(4):
                if visited[x][y][d]:
                    continue
                
                cnt = 0
                nx, ny = x, y
                while not visited[nx][ny][d]:
                    visited[nx][ny][d] = True
                    cnt += 1
                    
                    if grid[nx][ny] == 'L':
                        d = (d - 1) % 4
                    elif grid[nx][ny] == 'R':
                        d = (d + 1) % 4
                    
                    nx = (nx + dxy[d][0]) % n
                    ny = (ny + dxy[d][1]) % m
                ans.append(cnt)
                    
    return sorted(ans)