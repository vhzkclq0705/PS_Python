# Silver 5 - 누울 자리를 찾아라

import sys
input = sys.stdin.readline

def rotate():
    tmp = zip(*room[::-1])
    return [str(i) for i in tmp]

def check(matrix):
    cnt = 0
    for i in matrix:
        for j in i.split('X'):
            if j.count('.') >= 2:
                cnt += 1
    
    return cnt

room = [input().rstrip() for _ in range(int(input()))]
print(check(room), check(rotate()))