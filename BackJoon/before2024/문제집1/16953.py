# Silver 2 - A -> B

def solution(a, b):
    ans = 0
    while b:
        ans += 1
        if a == b:
            return ans
        if b % 2 == 0:
            b //= 2
        elif b % 10 == 1:
            b //= 10
        else:
            return -1
    return -1

a, b = map(int, input().split())
print(solution(a, b))