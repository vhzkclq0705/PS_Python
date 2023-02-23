# Silver 2 - 주식

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    MAX = 0
    ans = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] > MAX:
            MAX = s[i]
        else:
            ans += MAX - s[i]
    
    print(ans)