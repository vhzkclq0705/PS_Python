# Silver 3 - 햄버거 분배

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(lambda x: 0 if x == 'H' else 1, input().rstrip()))
ans = 0

for i in range(n):
    if s[i] == 1:
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and s[j] == 0:
                s[j] = -1
                ans += 1
                break

print(ans)