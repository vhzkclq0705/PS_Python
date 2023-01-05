# Gold 4 - 스도쿠

board = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

def check_Row(x, n):
    return False if n in board[x] else True

def check_Col(y, n):
    for i in range(9):
        if board[i][y] == n:
            return False
    return True

def check_Rect(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if board[i + nx][j + ny] == n:
                return False
    return True

def bt(depth):
    if depth == len(blank):
        for i in board:
            print(*i)
        exit(0)
    
    for i in range(1, 10):
        x = blank[depth][0]
        y = blank[depth][1]

        if check_Row(x, i) and check_Col(y, i) and check_Rect(x, y, i):
            board[x][y] = i
            bt(depth + 1)
            board[x][y] = 0

bt(0)