# LEVEL 1

def solution(board, moves):
    n = len(board)
    board = [[board[j][i] for j in range(n) if board[j][i]][::-1] for i in range(n)]
    stack = []
    ans = 0

    for i in moves:
        if board[i-1]:
            doll = board[i-1].pop()
            if stack and stack[-1] == doll:
                stack.pop()
                ans += 2
            else:
                stack.append(doll)
            
    return ans