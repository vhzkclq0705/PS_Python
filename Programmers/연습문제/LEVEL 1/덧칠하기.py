# LEEL 1

def solution(n, m, section):
    p, ans = 0, 0
    
    for i in range(len(section)):
        if section[i] < p:
            continue
        
        ans += 1
        p = section[i] + m
    
    return ans