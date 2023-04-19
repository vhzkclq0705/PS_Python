# LEVEL 2

def solution(board):
    ans = board[0][0]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                ans = max(ans, board[i][j])

    return ans ** 2