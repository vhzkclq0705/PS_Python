# Silver 5 - 기상캐스터

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = [input().rstrip() for _ in range(h)]

for i in board:
    flag = False
    cnt = 0

    for j in i:
        if j == 'c':
            print(0, end=' ')
            flag = True
            cnt = 0
        else:
            if not flag:
                print(-1, end=' ')
            else:
                cnt += 1
                print(cnt, end=' ')
    print()