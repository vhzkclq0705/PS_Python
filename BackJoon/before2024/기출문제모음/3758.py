# Silver 3 - KCPC

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(m)]
    board = [[0] * k for _ in range(n)]
    cnt, last = [0] * n, [0] * n
    ans = []

    for i in range(m):
        team, p, score = s[i]
        cnt[team - 1] += 1
        last[team - 1] = i
        board[team - 1][p - 1] = max(board[team - 1][p - 1], score)
    
    for i in range(n):
        ans.append([sum(board[i]), cnt[i], last[i], i])
    
    ans.sort(key=lambda x:(-x[0], x[1], x[2]))

    for i in range(n):
        if ans[i][3] == t - 1:
            print(i + 1)
            break