# LEVEL 1

def solution(t, p):
    l = len(p)
    ans = 0
    
    for i in range(0, len(t) - l + 1):
        if int(t[i:i+l]) <= int(p):
            ans += 1
    
    return ans