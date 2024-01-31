# Silver 2 - 폴짝폴짝

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
a, b = map(lambda x: int(x) - 1, input().split())
q = deque([(a, 0)])
visited = [False] * n
visited[a] = True
ans = -1

while q:
    p, cnt = q.popleft()
    
    if p == b:
        ans = cnt
        break
    
    cnt += 1
    for i in range(p + s[p], n, s[p]):
        if not visited[i]:
            q.append((i, cnt))
    for i in range(p - s[p], -1, -s[p]):
        if not visited[i]:
            q.append((i, cnt))

print(ans)