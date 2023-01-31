# Silver 2 - 종이의 개수

import sys
input = sys.stdin.readline

def cut(x, y, n):
    num = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        cut(x + k * n // 3, y + l * n // 3, n // 3)
                return
    
    ans[num + 1] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = [0] * 3

cut(0, 0, n)
[print(i) for i in ans]