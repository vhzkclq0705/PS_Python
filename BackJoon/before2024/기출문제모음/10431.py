# Silver 5 - 줄세우기

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = list(map(int, input().split()))
    n = s[0]
    t = s[1:]
    cnt = 0
    
    for i in range(20):
        for j in range(i):
            if t[j] > t[i]:
                num = t[i]
                tmp = t[j:i]
                t[j] = num
                t[j + 1: i + 1] = tmp
                cnt += len(tmp)
    
    print(n, cnt)