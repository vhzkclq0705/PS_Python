from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[-1] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(characterX, characterY)])
    visited[characterX][characterY] = True
    ans = 0
    
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x - 1, rect)
        for x in range(x1, x2 * 2 + 1):
            for y in range(y1, y2 * 2 + 1):
                if board[x][y] == -1:
                    board[x][y] = 1
                elif board[x][y] == 0:
                    board[x][y] = 0
                if x1 < x < x2 * 2 and y1 < y < y2 * 2:
                    board[x][y] = 0
    
    for i in range(102):
        for j in range(102):
            print(board[i][j], end=' ')
        print()
    
    for x in range(102):
        for y in range(102):
            if board[x][y] == 1:
                q.append((x, y))
    
    while q:
        x, y = q.popleft()
        if x == itemX and y == itemY:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= 101 and 0 <= ny <= 101 and not visited[nx][ny] and board[x][y] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                ans += 1

    return ans // 2

rect = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
cx = 1
cy = 3
ix = 7
iy = 8
print(solution(rect, cx, cy, ix, iy))