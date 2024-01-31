# Silver 1 - IOIOI

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
idx = cnt = ans = 0

while idx < m - 2:
    if s[idx:idx + 3] == 'IOI':
        idx += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(ans)