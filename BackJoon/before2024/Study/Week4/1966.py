# Silver 3 - 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = deque(map(int, input().split()))
    idx = deque([0] * (n))
    idx[m] = 1
    ans = 0
    
    while True:
        max_p = max(s)
        first = s.popleft()
        i = idx.popleft()

        if first == max_p:
            ans += 1
            if i:
                print(ans)
                break
        else:
            s.append(first)
            idx.append(i)