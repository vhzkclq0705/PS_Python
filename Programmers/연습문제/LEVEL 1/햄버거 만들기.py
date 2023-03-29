# LEVEL 1

def solution(ingredient):
    s = []
    ans = 0
    
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            ans += 1
            for _ in range(4):
                s.pop()
    
    return ans