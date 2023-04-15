# LEVEL 2

def solution(r1, r2):
    ans = 0

    for i in range(1, r2 + 1):
        a = int((r2 ** 2 - i ** 2) ** .5)
        if i >= r1:
            ans += a + 1
        else:
            b = int((r1 ** 2 - i ** 2) ** .5)
            if b ** 2 + i ** 2 == r1 ** 2:
                ans += a - b + 1
            else:
                ans += a - b

    return ans * 4