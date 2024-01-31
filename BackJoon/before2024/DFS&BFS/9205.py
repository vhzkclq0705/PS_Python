# Gold 5 - 맥주 마시면서 걸어가기

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()

        if abs(feX - x) + abs(feY - y) <= 1000:
            return True
        
        for i in range(n):
            if abs(store[i][0] - x) + abs(store[i][1] - y) <= 1000 and not visited[i]:
                q.append((store[i][0], store[i][1]))
                visited[i] = True
    
    return False

for _ in range(int(input())):
    n = int(input())
    homeX, homeY = map(int, input().split())
    store = ([list(map(int, input().split())) for _ in range(n)])
    feX,feY = map(int, input().split())
    visited = [False] * n
    q = deque([(homeX, homeY)])
    
    print('happy' if bfs() else 'sad')