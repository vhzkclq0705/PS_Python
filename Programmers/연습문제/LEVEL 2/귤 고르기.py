# LEVEL 2

from collections import Counter

def solution(k, tangerine):
    t = [v for k, v in sorted(Counter(tangerine).items(), key=lambda x: x[1])]
    tmp = 0
    ans = 0
    
    while tmp < k:
        tmp += t.pop()
        ans += 1
        
    return ans