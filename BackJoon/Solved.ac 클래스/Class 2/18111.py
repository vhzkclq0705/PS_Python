# Silver 2 - 마인크래프트

from collections import Counter
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = []
for _ in range(n):
    board += map(int, input().split())
board.sort()

low, high = board[0], board[-1]
ans, height = sys.maxsize, 0
board = dict(Counter(board))

for h in range(low, high + 1):
    dig, pull = 0, 0
    
    for i in board:
        if i > h:
            dig += (i - h) * board[i]
        else:
            pull += (h - i) * board[i]
    
    if b + dig - pull < 0:
        continue

    time = dig * 2 + pull
    if time <= ans:
        ans = time
        height = h

print(ans, height)