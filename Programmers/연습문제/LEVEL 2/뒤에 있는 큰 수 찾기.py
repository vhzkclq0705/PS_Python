# LEVEL 2

def solution(numbers):
    ans = [-1] * len(numbers)
    stack = []
    
    for idx, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            ans[stack.pop()] = n
        stack.append(idx)
    
    return ans