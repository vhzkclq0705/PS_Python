# LEVEL 2

def solution(s):
    idx = 0
    cnt = 0
    
    while s != '1':
        l = len(s)
        a = s.count('1')
        cnt += l - a
        s = bin(a)[2:]
        idx += 1
    
    return [idx, cnt]