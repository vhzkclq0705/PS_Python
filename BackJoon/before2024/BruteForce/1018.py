# Silver 4 - 체스판 다시 칠하기

n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = []

for i in range(n - 7):
    for j in range(m - 7):
        start_W = 0
        start_B = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        start_B += 1
                    if board[a][b] != 'B':
                        start_W += 1
                else:
                    if board[a][b] != 'B':
                        start_B += 1
                    if board[a][b] != 'W':
                        start_W += 1
        
        result.append(min(start_W, start_B))

print(min(result))