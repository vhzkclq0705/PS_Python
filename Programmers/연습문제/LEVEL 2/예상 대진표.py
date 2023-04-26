# LEVEL 2

def solution(n,a,b):
    ans = 0

    while a != b:
        ans += 1
        a = (a+1)//2
        b = (b+1)//2

    return ans