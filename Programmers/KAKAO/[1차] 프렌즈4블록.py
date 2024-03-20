# LEVEL2

def solution(m, n, board):
    answer = 0
    board = [list(i) for i in zip(*board)][::-1]
    m, n = n, m
    visited = set()
    
    while True:
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] and board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1]:
                    visited.update({(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)})
        
        if visited:
            answer += len(visited)
            for x, y in visited:
                board[x][y] = ''
            visited.clear()
        else:
            break
        
        for x in range(m):
            tmp = [board[x][y] for y in range(n - 1, -1, -1) if board[x][y]]
            for y in range(n):
                board[x][y] = '' if y < n - len(tmp) else tmp.pop()
                
    return answer