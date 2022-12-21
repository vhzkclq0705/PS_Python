# LEVEL 2

def convert(n, k):
    num = ''
    while n >= k:
        num += str(n % k)
        n //= k
    num += str(n % k)
    
    return num[::-1]

def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return False if n == 1 else True

def solution(n, k):
    answer = 0

    for num in convert(n, k).split("0"):
        if num == '':
            continue
        if isPrime(int(num)):
            answer += 1

    return answer

n = 437674
k = 3
print(solution(n, k))

n = 110011
k = 10
print(solution(n, k))