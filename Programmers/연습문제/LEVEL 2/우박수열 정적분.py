# LEVEL 2

def solution(k, ranges):
    ans = []
    area = [0.0]
    
    while k != 1:
        tmp = k // 2 if k % 2 == 0 else k * 3 + 1
        area.append(area[-1] + (k + tmp) / 2)
        k = tmp
    
    for s, e in ranges:
        r = len(area) - 1 + e
        ans.append(-1 if s > r else area[r] - area[s])
    
    return ans