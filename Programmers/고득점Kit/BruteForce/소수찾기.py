# Level 2

import math
from itertools import permutations

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True if n > 1 else False

def solution(numbers):
    ans = 0
    temp = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            temp.add(int(''.join(p)))

    for i in temp:
        if is_prime_num(i):
            ans += 1
            
    return ans

numbers = "011"
print(solution(numbers))