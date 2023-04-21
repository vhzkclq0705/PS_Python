# LEVEL 2

from collections import defaultdict, Counter

def solution(topping):
    a = defaultdict(int)
    b = dict(Counter(topping))
    ans = 0
    
    for i in topping:
        a[i] += 1
        b[i] -= 1
        
        if b[i] == 0:
            del b[i]
        
        if len(a) == len(b):
            ans += 1
    
    return ans