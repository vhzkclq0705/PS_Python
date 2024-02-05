# Silver 4 - 체스판 다시 칠하기

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
ans = 2500

for i in range(n - 7):
    for j in range(m - 7):
        cnt_a, cnt_b = 0, 0

        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r + c) % 2 == 0:
                    if board[r][c] == 'B':
                        cnt_a += 1
                    else:
                        cnt_b += 1
                else:
                    if board[r][c] == 'W':
                        cnt_b += 1
                    else:
                        cnt_a += 1
        
        ans = min(ans, cnt_a, cnt_b)

print(ans)                     