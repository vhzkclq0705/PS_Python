# LEVEL 1

from collections import Counter

def solution(N, stages):
    ans = {i:0 for i in range(1, N+1)}
    s = dict(Counter(stages))
    l = len(stages)
    
    for i in range(1, N+1):
        if i in s:
            ans[i] = s[i]/l
            l -= s[i]
    
    return sorted(ans, key=lambda x:ans[x], reverse=True)