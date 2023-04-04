# LEVEL 1

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        c = n // a
        d = n % a
        answer += c * b
        n = d + c * b
        
    return answer