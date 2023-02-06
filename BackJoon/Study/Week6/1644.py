# Gold 3 - 소수의 연속합

import sys
input = sys.stdin.readline

def make_Primes(n):
    nums = [True] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if nums[i]:
            for j in range(i * 2, n + 1, i):
                nums[j] = False
    
    return [i for i in range(2, n + 1) if nums[i]] + [0]

n = int(input())
prime = make_Primes(n)
l = len(prime)
ans, left, right = 0, 0, 0
SUM = prime[0]

while left < l - 1 and right < l - 1:
    if SUM < n:
        right += 1
        SUM += prime[right]
    elif SUM > n:
        SUM -= prime[left]
        left += 1
    else:
        ans += 1
        right += 1
        SUM += prime[right]

print(ans)