# LEVEL 1

def check(n):
    s = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
        
    return len(s)

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if check(i) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer