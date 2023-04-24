# LEVEL 2

from collections import Counter

def solution(want, number, discount):
    d = {want[i]:number[i] for i in range(len(want))}
    dis = dict(Counter(discount[:10]))
    left, right = 0, 9
    ans = 0
    
    while right < len(discount) - 1:
        if d == dis:
            ans += 1
        
        dis[discount[left]] -= 1
        if dis[discount[left]] == 0:
            del dis[discount[left]]
        left += 1
        
        right += 1
        if discount[right] not in dis:
            dis[discount[right]] = 1
        else:
            dis[discount[right]] += 1
        
    return ans if d != dis else ans + 1