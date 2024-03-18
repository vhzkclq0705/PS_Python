# LEVEL 1 / 10번 / 이웃한 칸

def solution(board, x, y):
    answer = 0
    n = len(board)
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and board[x][y] == board[nx][ny]:
            answer += 1

    return answer