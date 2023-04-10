# LEVEL 1

def solution(d, budget):
    total = sum(d)
    d.sort()
    
    while total > budget:
        total -= d.pop()
    
    return len(d)