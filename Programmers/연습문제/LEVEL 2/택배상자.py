# LEVEL 2

from collections import deque

def solution(order):
    n = deque(range(1, len(order) + 1))
    stack = []
    ans = 0
    
    for i in order:
        if stack and stack[-1] == i:
            ans += 1
            stack.pop()
            continue
        
        while n and n[0] != i:
            stack.append(n.popleft())
        if n and n[0] == i:
            ans += 1
            n.popleft()
            continue
        
        if stack[-1] != i:
            return ans
        
    return ans