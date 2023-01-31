# Silver 1 - 쿼드트리

import sys
input = sys.stdin.readline

def compress(x, y, n):
    num = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != matrix[i][j]:
                print('(', end='')
                for k in range(2):
                    for l in range(2):
                        compress(x + k * n // 2, y + l * n // 2, n // 2)
                print(')', end='')
                return

    print(num, end='')

n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
compress(0, 0, n)