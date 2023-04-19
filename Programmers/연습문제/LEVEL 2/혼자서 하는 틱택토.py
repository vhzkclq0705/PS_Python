# LEVEL 2

def check(board, ch):
    for i in board:
        if i.count(ch) == 3:
            return True

    for i in zip(*board):
        if list(i).count(ch) == 3:
            return True

    if board[0][0] == board[1][1] == board[2][2] == ch or board[0][2] == board[1][1] == board[2][0] == ch:
        return True

    return False

def solution(board):
    cnt_O, cnt_X = 0, 0
    res_O, res_X = check(board, 'O'), check(board, 'X')

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt_O += 1
            elif board[i][j] == 'X':
                cnt_X += 1

    if cnt_O < cnt_X or cnt_O >= cnt_X + 2:
        return 0
    elif res_O and cnt_O != cnt_X + 1:
        return 0
    elif res_X and cnt_O != cnt_X:
        return 0

    return 1