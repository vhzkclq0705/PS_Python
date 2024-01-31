# Gold 5 - 소트 게임

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(input().split())
q = deque([(s, 0)])
d = {''.join(s)}
ans = -1

while q:
    per, cnt = q.popleft()
    if per == sorted(s):
        ans = cnt
        break

    for i in range(n - k + 1):
        temp = (per[i:i + k])[::-1]
        new_Per = per[:i] + temp + per[i + k:]
        hash_Per = ''.join(new_Per)
        
        if hash_Per not in d:
            d.add(hash_Per)
            q.append((new_Per, cnt + 1))

print(ans)