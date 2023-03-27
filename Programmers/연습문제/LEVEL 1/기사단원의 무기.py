# LEVEL 1

def weight(n, limit, power):
    s = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    
    return len(s) if len(s) <= limit else power

def solution(number, limit, power):
    return sum([weight(i, limit, power) for i in range(1, number + 1)])