# Silver 3 - 햄버거 분배

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(lambda x: 1 if x == 'H' else 2, input().rstrip()))
cnt = 0

for i in range(n):
    if s[i] == 2:
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and s[j] == 1:
                s[j] = 0
                cnt += 1
                break

print(cnt)