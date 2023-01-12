# Silver 2 - 언더프라임

import sys
input = sys.stdin.readline

def get_Primes(n):
    nums = [True] * n

    for i in range(2, int(n ** 0.5) + 1):
        if nums[i]:
            for j in range(2 * i, n, i):
                nums[j] = False
    
    return [i for i in range(2, n) if nums[i]]

def is_Underprime(n):
    num = []
    i = 2

    while i <= n:
        if n % i == 0:
            num.append(i)
            n //= i
        else:
            i += 1

    return 1 if len(num) in primes else 0

a, b = map(int, input().split())
primes = get_Primes(b)
cnt = 0

for i in range(a, b + 1):
    if i not in primes:
        cnt += is_Underprime(i)

print(cnt)
