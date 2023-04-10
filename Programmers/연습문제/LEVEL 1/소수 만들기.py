# LEVEL 1

from itertools import combinations

def primes(n):
    primes = [False] * 2 + [True] * (n - 1)
    
    for i in range(2, int(n**.5)+1):
        if primes[i]:
            for j in range(i*2, n+1, i):
                primes[j] = False
    
    return primes

def solution(nums):
    answer = 0
    prime = primes(sum(nums))
    
    for c in combinations(nums, 3):
        if prime[sum(c)]:
            answer += 1
    
    return answer