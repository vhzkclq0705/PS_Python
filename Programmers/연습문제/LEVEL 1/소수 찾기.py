# LEVEL 1

def solution(n):
    primes = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n ** .5) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    
    return sum(primes)