# Gold 5 - 문자열 게임 2

from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w = list(input().rstrip())
    k = int(input())
    d = dict(Counter(w))
    ans = []
    
    for key, value in d.items():
        if value >= k:
            tmp = list(filter(lambda x: w[x] == key, range(len(w))))
            
            for i in range(len(tmp) - k + 1):
                ans.append(tmp[i + k - 1] - tmp[i] + 1)
    
    if ans:
        print(min(ans), max(ans))
    else:
        print(-1)