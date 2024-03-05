# Silver 5 - 줄세우기

import sys
input = sys.stdin.readline

for t in range(int(input())):
    s = list(map(int, input().split()))[1:]
    ans = 0

    for i in range(20):
        for j in range(i):
            if s[j] > s[i]:
                tmp = s[i]
                s.remove(tmp)
                s.insert(j, tmp)
                ans += i - j
                break
    
    print(t + 1, ans)