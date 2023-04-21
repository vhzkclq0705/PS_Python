# LEVEL 2

from collections import defaultdict

def solution(weights):
    ans = 0
    d = defaultdict(int)
    
    for w in weights:
        ans += d[w] + d[w * 2] + d[w / 2]
        ans += d[w * 2 / 3] + d[w * 3 / 2]
        ans += d[w * 3 / 4] + d[w * 4 / 3]
        d[w] += 1
    
    return ans