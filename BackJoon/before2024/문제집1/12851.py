# Gold 4 - 숨바꼭질 2

from collections import deque

def bfs(n):
    q = deque([n])
    visited[n] = 0
    cnt = 0

    while q:
        x = q.popleft()

        if x == k:
            cnt += 1
            continue

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000:
                if visited[i] == 0 or visited[i] == visited[x] + 1:
                    visited[i] = visited[x] + 1
                    q.append(i)
    
    return cnt
                
n, k = map(int, input().split())
visited = [0] * 100001

ans = bfs(n)
print(visited[k])
print(ans)